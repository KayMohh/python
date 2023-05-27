## company blog / init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)



#################################################
####DB SetUp#####
################################
###############


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from companyblog.error_pages.handlers import error_pages
from companyblog.users.views import users
from companyblog.core.views import core



app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)

db = SQLAlchemy(app)
Migrate(app.db)





#############
##LoginManager


login_manager = LoginManager()

login_manager.init.app(app)
login_manager.login_view = 'users.login'
