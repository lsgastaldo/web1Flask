from flask import session, redirect, url_for, flash, render_template, Flask, request
from . import main
from .forms import ComentaryForm, NewsForm
from app.models import User, Role, Comentary, News
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.decorators import admin_required, permission_required


@main.route('/')
def index():
    index_news = News.query.all()
    return render_template("main/index.html", index_news=index_news)

@main.route('/listnews')
def listnews():
    page = request.args.get('page', 1, type=int)
    pagination = News.query.order_by(News.id).paginate(page, per_page=10, error_out=False)
    allnews = pagination.items
    return render_template("main/listnews.html", allnews=allnews, pagination=pagination)

@main.route('/news/<int:id>')
def news(id):
    news = News.query.filter_by(id=id).first()
    return render_template("main/news.html", news=news)

@main.route('/postnews', methods=['GET', 'POST'])
@login_required
@admin_required
def post_news():
    news = News()
    form = NewsForm()
    if form.validate_on_submit():
        news = News(
            title = form.title.data,
            index_body = form.index_body.data,
            body = form.body.data,
            img = form.img.data,
            author_id = current_user.id
            )
        db.session.add(news)
        db.session.commit()
        flash('News posted!')
        return redirect(url_for('main.news', id=news.id))
    return render_template('main/postnews.html', form=form, id=news.id)