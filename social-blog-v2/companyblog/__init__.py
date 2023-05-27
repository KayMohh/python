## company blog / init.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



#################################################
####DB SetUp#####
################################
###############


from companyblog.error_pages.handlers import error_pages

from companyblog.core.views import core

app.register_blueprint(core)
app.register_blueprint(error_pages)
