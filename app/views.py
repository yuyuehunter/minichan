from flask import render_template
from app import app

@app.route('/')
def index():
    return '<h1>minichan</h1>'
