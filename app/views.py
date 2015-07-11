from flask import render_template
from app import app
from app import db, models

def query_all_categories():
    cur = models.Category.query.all()
    categories = [dict(name=cat.name, url=cat.url_name) for cat in cur]
    return categories

def query_category_by_name(url):
    cur = models.Category.query.filter_by(url_name=url).first()

    category = {'id':cur.id, 'name':cur.name, 'url':cur.url_name}

    return category

def query_post(cat_id):
    cur = models.Post.query.filter_by(category_id=cat_id)

    posts = [dict(id=post.id, title=post.title, text=post.text) for post in cur]

    return posts

def query_comment(p_id):
    cur = models.Comment.query.filter_by(post_id=p_id)

    comments = [dict(id=com.id, comment=com.comment, pid=com.post_id) for com in cur]

    return comments

@app.route('/')
def index():
    return render_template('index.html', categories=query_all_categories())

@app.route('/<cat>')
def show_category(cat):
    category = query_category_by_name(cat)
    posts = query_post(category['id'])

    allcomm = []

    for p in posts:
        comments = query_comment(p['id'])
        allcomm.append(comments)

    return render_template('board.html', category=category, posts=posts, comments=comments, allcomm=allcomm)
