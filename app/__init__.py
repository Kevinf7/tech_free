from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect
from config import Config
from app.breadcrumb import Breadcrumb


db = SQLAlchemy()
# compare_type = true - this is so that flask migrate detect changes to columns like size
migrate = Migrate(compare_type=True)
moment = Moment()
# login_manager = LoginManager()
csrf = CSRFProtect()

breadcrumb = Breadcrumb()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        # login_manager.init_app(app)
        migrate.init_app(app,db)
        moment.init_app(app)
        csrf.init_app(app)

        '''
        from app.admin_auth import bp as admin_auth_bp
        app.register_blueprint(admin_auth_bp, url_prefix='/admin')

        from app.admin_main import bp as admin_main_bp
        app.register_blueprint(admin_main_bp, url_prefix='/admin')

        from app.admin_message import bp as admin_message_bp
        app.register_blueprint(admin_message_bp, url_prefix='/admin')

        from app.admin_page import bp as admin_page_bp
        app.register_blueprint(admin_page_bp, url_prefix='/admin')

        from app.admin_media import bp as admin_media_bp
        app.register_blueprint(admin_media_bp, url_prefix='/admin')

        '''

        from app.admin_errors import bp as errors_bp
        app.register_blueprint(errors_bp)
        
        from app.email import bp as email_bp
        app.register_blueprint(email_bp)

        from app.main import bp as main_bp
        app.register_blueprint(main_bp)

        # breadcrumb.init_app(app)

    return app
