import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "admin"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
    UPLOAD_FOLDER = '/app/static/news'
    ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg'])
    DEBUG = True


    @staticmethod
    def init_app(app):
        pass
