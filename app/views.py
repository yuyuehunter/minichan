from flask import render_template
from app import app
from app import db, models

def query_all_categories():
    cur = models.Category.query.all()
    categories = [dict(name=cat.name, url=cat.url_name) for cat in cur]
    return categories

def query_category_by_name(url):
    cur = models.Category.query.filter_by(url_name=url).first()

    return cur.name

@app.route('/')
def index():
    return render_template('index.html', categories=query_all_categories())

@app.route('/<cat>')
def show_category(cat):
    return query_category_by_name(cat)
