from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    url_name = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % (self.name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32))
    title = db.Column(db.String(64))
    text = db.Column(db.String(10240))
    time = db.Column(db.DateTime)
    file = db.Column(db.String(1024))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Post %r>' % (self.post)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32))
    comment = db.Column(db.String(10240))
    time = db.Column(db.DateTime)
    file = db.Column(db.String(1024))

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.comment)
