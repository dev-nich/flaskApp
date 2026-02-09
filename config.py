import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev.christines'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' +  os.path.join(basedir, 'app.db')
    POSTS_PER_PAGE=10
    MAIL_SERVER=os.environ.get('MAIL_SERVER') or ''
    MAIL_PORT=os.environ.get('MAIL_PORT') or ''
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') or ''
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME') or ''
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD') or ''
    MAIL_DEFAULT_SENDER=os.environ.get('MAIL_DEFAULT_SENDER') or ''
    ADMINS=os.environ.get('ADMINS') or None