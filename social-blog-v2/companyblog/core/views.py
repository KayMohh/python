## core views
from companyblog.models import Blogpost
from flask import render_template, request, Blueprint

core = Blueprint("core", __name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    blog_posts= Blogpost.query.order_by(Blogpost.data.desc()).paginate(page=page,per_page=3)
    return render_template('index.html', blog_posts=blog_posts)


    return render_template ('index.html')


@core.route('/info')
def info():

    return render_template('info.html')
