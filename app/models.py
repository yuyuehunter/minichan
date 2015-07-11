from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    url_name = db.Column(db.String(32), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % (self.name)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(10240))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.comment)
