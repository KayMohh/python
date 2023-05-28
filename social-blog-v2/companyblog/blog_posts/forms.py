## blog posts

from flask_wtf import FlaskForm
from wtforms import StringField, Submit =FIeld, TextAreaField
from wtforms.validators import DataRequired

class BlogpostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Blogpost')
