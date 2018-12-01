from app import db
from datetime import datetime
import re



def slugify(text):
	"Задача: взять строку и заменить все не используемые символы в адресной строке на симовол - "
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', text)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.String(1000))
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.slug = slugify(self.title)
		

