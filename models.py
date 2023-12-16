from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    password = db.Column(db.String)

Base.metadata.create_all(engine)

class Author(Base):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    posts = db.orm.relationship(back_populates='author')

class Post(Base):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.orm.relationship(back_populates='posts')

post_comment = db.Table(
    'post_comments',
    Base.metadata,
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('comment_id', db.Integer, db.ForeignKey('comments.id')),
)

class Post(Base):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.orm.relationship(back_populates='posts')
    comments = db.orm.relationship(
        'Comment', secondary=post_comment, back_populates='posts'
    )

class Comment(Base):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.orm.relationship(back_populates='posts')
    posts = db.orm.relationship(
        'Post', secondary=post_comment, back_populates='comments'
    )
  
