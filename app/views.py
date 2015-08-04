import datetime
import os
import random
from flask import render_template, request, redirect
from app import app
from app import db, models
from app import queries
from app import allowed_filename
from werkzeug import secure_filename

def format_time(time):
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    cur_day = time.weekday()

    time_str = str(time.month) + '/' + str(time.day) + '/' + str(time.year) + '(' + weekdays[cur_day] + ')' + str(time.hour) + ':' + str(time.minute) + ':' + str(time.second)

    return time_str

def random_logo():
    images = ['claude.jpg', 'russian_kid.png', 'shia.jpg', 'tom.jpg', 'welcome_internet.jpg']
    return images[random.randint(0, len(images)-1)]

@app.route('/')
def index():
    return render_template('index.html', categories=queries.query_all_categories())

@app.route('/<cat>/', methods=['GET', 'POST'])
def show_category(cat):
    category = queries.query_category_by_name(cat)
    posts = queries.query_post(category['id'])

    if category['id'] == '' or category['name'] == '' or category['url'] == '':
        return render_template('404.html')

    allcomm = []

    for p in posts:
        allcomm.append(queries.query_comment(p['id']))

    thread_data = {
        'name': '',
        'subject': '',
        'comment': '',
    }

    if request.method == 'POST':
        thread_data['name'] = request.form['name']
        thread_data['subject'] = request.form['subject']
        thread_data['comment'] = request.form['comment']
        file = request.files['file']
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        post_time = datetime.datetime.utcnow()

        if thread_data['name'] == '':
            thread_data['name'] = 'Anonymous'

    if thread_data['comment'] != '':
        thread = models.Post(author=thread_data['name'], title=thread_data['subject'], text=thread_data['comment'], time=post_time, file=filename, category_id=category['id'])
        db.session.add(thread)
        db.session.commit()
        return redirect(cat, code=302)
    
    return render_template('board.html', category=category, posts=posts, allcomm=allcomm, cat=cat)

@app.route('/<cat>/thread/<thread_id>', methods=['GET', 'POST'])
def show_thread(cat, thread_id):
    post = models.Post.query.get(thread_id)
    allcomm = queries.query_comment(post.id)

    comment_data = {
        'name': '',
        'comment': ''
    }

    filename = ''

    if request.method == 'POST':
        comment_data['name'] = request.form['name']
        comment_data['comment'] = request.form['comment']
        comment_time = datetime.datetime.utcnow()
        file = request.files['file']
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        if comment_data['name'] == '':
            comment_data['name'] = 'Anonymous'

    if comment_data['comment'] != '':
        comment = models.Comment(author=comment_data['name'], comment=comment_data['comment'], time=comment_time, file=filename, post_id=thread_id)
        db.session.add(comment)
        db.session.commit()
        return redirect(cat, code=302)
    
    return render_template('thread.html', post=post, allcomm=allcomm)
