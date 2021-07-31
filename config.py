import os
from dotenv import load_dotenv
from pathlib import Path


basedir = Path(__file__).parent
load_dotenv(basedir / '.env')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'random string'
    
    if (os.environ.get('FLASK_ENV') == 'development'):
        # Dev only so browser doesnt cache for CSS
        SEND_FILE_MAX_AGE_DEFAULT = 0
        # auto reload template without needing to restart Flask
        TEMPLATES_AUTO_RELOAD = True
        SERVER_NAME = 'localhost:5000'
    else:
        SERVER_NAME = 'thechintan123.pythonanywhere.com'
        SESSION_COOKIE_DOMAIN = False
        SESSION_COOKIE_SECURE = True
    
    #####

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # recommended by Pythonanywhere otherwise you get mysql timeout
    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Sendgrid settings
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    MAIL_FROM = os.environ.get('MAIL_FROM')
    MAIL_ADMINS = os.environ.get('MAIL_ADMINS').split(' ')

    ### ADMIN AUTH ###
    FORGOT_PASSWORD_TOKEN_EXPIRE = 3600  # in seconds, 3600 = 1 hour

    ### ADMIN MESSAGE ###
    ADMIN_MESSAGE = True
    MESSAGES_PER_PAGE = 10

    ### ADMIN PAGE ###
    ADMIN_PAGE = False
    PAGES_PER_PAGE = 10
    UPLOAD_PATH_PAGE = basedir / 'app/static/uploads/page'
    UPLOAD_PATH_THUMB_PAGE = basedir / 'app/static/uploads/page/thumbnails'


