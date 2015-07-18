from flask import render_template, request
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

    posts = [dict(id=post.id, title=post.title, author=post.author, text=post.text) for post in cur]

    return posts

def query_comment(p_id):
    cur = models.Comment.query.filter_by(post_id=p_id)

    comments = [dict(id=com.id, comment=com.comment, pid=com.post_id) for com in cur]

    return comments

@app.route('/')
def index():
    return render_template('index.html', categories=query_all_categories())

@app.route('/<cat>/', methods=['GET', 'POST'])
def show_category(cat):
    category = query_category_by_name(cat)
    posts = query_post(category['id'])

    allcomm = []

    for p in posts:
        allcomm.append(query_comment(p['id']))

    thread_data = {
        'name': '',
        'subject': '',
        'comment': ''
    }

    if request.method == 'POST':
        thread_data['name'] = request.form['name']
        thread_data['subject'] = request.form['subject']
        thread_data['comment'] = request.form['comment']

        if thread_data['name'] == '':
            thread_data['name'] = 'Anonymous'

    if thread_data['subject'] != '' and thread_data['comment'] != '':
        thread = models.Post(author=thread_data['name'], title=thread_data['subject'], text=thread_data['comment'], category_id=category['id'])
        db.session.add(thread)
        db.session.commit()
    
    return render_template('board.html', category=category, posts=posts, allcomm=allcomm, cat=cat)
