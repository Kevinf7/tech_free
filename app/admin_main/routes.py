from flask import render_template, g
from sqlalchemy import desc
from flask_login import current_user, login_required
from app.admin_main import bp
from app.admin_page.models import Page
from app.admin_media.models import Images
from app.admin_message.models import Message
from app.breadcrumb import set_breadcrumb


# ADMIN MAIN routes

@bp.route('/')
@bp.route('/index')
@login_required
@set_breadcrumb('home')
def index():
    last_login = current_user.last_seen
    total_pages = Page.query.count()
    page_latest = Page.query.order_by(desc(Page.last_publish_date)).first()
    total_media = Images.query.count()
    total_message = Message.query.count()
    new_message = Message.query.filter(Message.create_date>=last_login).count()
    image_latest = Images.query.order_by(desc(Images.create_date)).limit(3).all()
    
    return render_template('admin_main/index.html', total_pages=total_pages, \
        total_media=total_media, total_message=total_message, new_message=new_message, \
        page_latest=page_latest, image_latest=image_latest)
    

@bp.route('/about', methods=['GET'])
@login_required
@set_breadcrumb('home about')
def about():
    return render_template('admin_main/about.html')


# Used by breadcrumbs
@bp.app_context_processor 
def inject_breadcrumb():
    breadcrumb = getattr(g, 'breadcrumb', '')
    return dict(breadcrumb=breadcrumb)


