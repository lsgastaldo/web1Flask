from flask import session, redirect, url_for, flash, render_template, Flask
from . import main
# from .forms import PostForm, NewsForm
# from app.models import Post, News
from app.models import User, Role
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.decorators import admin_required, permission_required


@main.route('/')
def index():
    return render_template("main/index.html")

# @main.route('/news/<int:id>')
# def news(id):
#     news = News.query.filter_by(id=id).first()
#     return render_template("main/news.html", news=news.id )

# @main.route('/postnews')
# @login_required
# @admin_required
# def post_news():
#     form = NewsForm()
#     if form.validate_on_submit():
#         form = NewsForm(
#             title = form.title.data,
#             index_body = form.index_body.data,
#             body = form.body.data,
#             img = form.img.data,
#             author_id = current_user.id
#             )
#         db.session.add(form)
#         db.session.commit()
#         flash('News posted!')
#         return redirect(url_for('main.news', form=form))
#     return render_template('main/postnews', form=form)