import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev.christines'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' +  os.path.join(basedir, 'app.db')
    POSTS_PER_PAGE=3
    ADMINS=[
        'dev.christines@gmail.com'
    ]
    MAIL_SERVER=os.environ.get('MAIL_SERVER')
    MAIL_PORT=os.environ.get('MAIL_PORT')
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER')
