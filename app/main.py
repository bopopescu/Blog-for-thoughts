from app import app
import view
from blog.blueprint import blog

app.register_blueprint(blog, url_prefix='/blog')

if __name__ == '__main__':
	app.run()