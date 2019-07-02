from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import Required, DataRequired, Length
from app.models import User, Role, News, Comentary
from werkzeug.utils import secure_filename
import config

class ComentaryForm(FlaskForm):
    body = TextAreaField('What do you think about it?', validators=[DataRequired()])
    submit = SubmitField('Submit !')

class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    index_body = StringField('Resumo', validators=[DataRequired()])
    body = TextAreaField('News', validators=[DataRequired()])
    img = StringField('Path to file')
    submit = SubmitField('Submit !')

    # def allowed_file(self, filename):
    #     return filename.rsplit('.').[1].lower() in config.ALLOWED_EXTENSIONS
