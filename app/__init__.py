import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename

UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'gif', 'gifv', 'jpg', 'jpeg', 'webm', 'mp4'])

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def check_extension(filename):
    ext = filename.split('.')
    ext = ext[len(ext)-1]
    return ext

from app import views, models

app.jinja_env.globals.update(format_time=views.format_time)
app.jinja_env.globals.update(query_comment=queries.query_comment)
app.jinja_env.globals.update(query_all_categories=queries.query_all_categories)
app.jinja_env.globals.update(query_thread_file=queries.query_thread_file)
app.jinja_env.globals.update(query_comment_file=queries.query_comment_file)
app.jinja_env.globals.update(check_extension=check_extension)
app.jinja_env.globals.update(random_logo=views.random_logo)
