from flask import Blueprint, render_template
from models import Post

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
def main_blog():
	return render_template('blog/main_blog.html')


@blog.route('/some_post')
def some_post():
	return 'Some post'

@blog.route('/<slug>')
def post_show(slug):
	post = Post.query.filter(Post.slug==slug).first()
	return render_template('blog/post_show.html', post=post)

@blog.route('/all_posts')
def all_posts():
	posts = Post.query.all()
	return render_template('blog/all_posts.html', posts=posts)