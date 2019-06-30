from flask import session, redirect, url_for, flash, render_template, request
from . import auth
from .forms import LoginForm, UserRegistrationForm, RoleForm, EditAdminProfileForm,\
    EditUserProfileForm, ValidationError
from app.models import User, Role
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.decorators import admin_required, permission_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.userpassword.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or passoword.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out !')
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['GET', 'POST'])
def user_registration():
    role = Role.query.filter_by(default=True).first()
    form = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            name=form.name.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password=form.userpassword.data,
            role_id=role.id
            )
        db.session.add(user)
        db.session.commit()
        flash('Registration Successfull!')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)

@auth.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('auth/profile.html', user=user) 

@auth.route('/addrole', methods=['GET', 'POST'])
@login_required
@admin_required
def addrole():
    form = RoleForm()
    roles = Role.query.all()
    if form.validate_on_submit():
        new_role = Role()
        new_role.name = form.name.data
        db.session.add(new_role)
        db.session.commit()
        flash('Função cadastrada com sucesso.')
        return redirect(url_for('auth.addrole'))
    return render_template('auth/addrole.html', form=form, roles=roles)

    def validate_name(self, field):
        role = Role.query.filter_by(name=field.data).first()
        if role:
            raise ValidationError('Role already in use!')

@auth.route('/editprofile', methods=['GET', 'POST'])
@login_required
def edit_profile_user():
    form = EditUserProfileForm()
    if form.validate_on_submit():
        current_user.name=form.name.data
        current_user.lastname=form.lastname.data
        current_user.email=form.email.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Perfil editado com sucesso!')
        return redirect(url_for('auth.profile', username=current_user.username))
    form.name.data=current_user.name
    form.lastname.data=current_user.lastname
    form.email.data=current_user.email
    return render_template('auth/editprofile.html', form=form, username=current_user.username)

@auth.route('/editprofile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditAdminProfileForm(user=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.name = form.name.data
        print(user.name, form.name.data)
        user.lastname = form.lastname.data
        user.email = form.email.data
        user.role_id = form.role_id.data
        db.session.add(user)
        db.session.commit()
        flash('Usuário editado com sucesso!')
        return redirect(url_for('auth.profile', username=user.username))
    form.username.data = user.username
    form.name.data = user.name
    form.lastname.data = user.lastname
    form.email.data = user.email
    form.role_id.data = user.role_id
    return render_template('auth/editprofile.html', form=form, username=user.username)

@auth.route('/userlist', methods=['GET', 'POST'])
@login_required
@admin_required
def list_user():
    users = User.query.all()
    return render_template('auth/userlist.html', users=users)

