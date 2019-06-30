from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, ValidationError, SelectField,\
    TextAreaField
from wtforms.validators import Required, DataRequired, Email, EqualTo, Length
from app.models import User, Role

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    userpassword = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class UserRegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[Email()])
    userpassword = PasswordField("Password", validators=[DataRequired()])
    confpassword = PasswordField("Confirm Password", validators=[
        EqualTo('userpassword', message="Passwords don't match")])
    submit = SubmitField("Sign up!")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")

class RoleForm(FlaskForm):
    name = StringField('Role', validators=[
        DataRequired()
    ])
    submit = SubmitField('Submit')

class EditUserProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[Email()])
    submit = SubmitField('Enviar')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use!')

class EditAdminProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    name = StringField('Name', validators=[DataRequired(), Length(1, 64)])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[Email()])
    role_id = SelectField('Role', coerce=int)
    submit = SubmitField("Save changes!")

    def __init__(self, user, *args, **kwargs):#role = backref
        super(EditAdminProfileForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [
            (role.id, role.name) for role in Role.query.order_by(Role.name).all()
        ]
        self.user = user
    
    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use!')