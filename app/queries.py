from app import db, models

def query_all_categories():
    cur = models.Category.query.all()
    categories = [dict(name=cat.name, url=cat.url_name) for cat in cur]
    return categories

def query_category_by_name(url):
    cur = models.Category.query.filter_by(url_name=url).first()

    if cur != None:
        category = {'id':cur.id, 'name':cur.name, 'url':cur.url_name}
        return category
    else:
        category = {'id':'', 'name':'', 'url':''}
        return category

def query_thread_file(id):
    cur = models.Post.query.get(id)
    file = cur.file

    return file

def query_comment_file(id):
    cur = models.Comment.query.get(id)
    file = cur.file

    return file

def query_post(cat_id):
    cur = models.Post.query.filter_by(category_id=cat_id)

    posts = [dict(id=post.id, title=post.title, author=post.author, text=post.text, time=post.time) for post in cur]

    return posts

def query_comment(p_id):
    cur = models.Comment.query.filter_by(post_id=p_id)

    comments = [dict(id=com.id, author=com.author, comment=com.comment, time=com.time, pid=com.post_id) for com in cur]

    return comments
