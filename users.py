from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'URL'
db = SQLAlchemy(app)


if __name__ == '__main__':

    user = User(name='John Doe')
    db.session.add(user)
    db.session.commit()

    post1 = Post(title='Post 1', content='Content 1', user=user)
    post2 = Post(title='Post 2', content='Content 2', user=user)
    db.session.add_all([post1, post2])
    db.session.commit()

    user_posts = user.posts

    for post in user_posts:
        print(post.title)

    app.run()
