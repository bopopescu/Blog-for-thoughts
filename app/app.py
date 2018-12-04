from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

# migrate
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Configuration)

# data base
db = SQLAlchemy(app)

# migrate
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

