
from flask import url_for, request, g
from functools import wraps


class Breadcrumb(object):
    map=[]
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        with app.app_context():
            '''
            Breadcrumb.map.append({'key': 'home', 'name': 'Home', 
                'url': url_for('admin_main.index'), 'icon': '<i class="fas fa-home"></i>'})
            Breadcrumb.map.append({'key': 'page', 'name': 'Pages', 
                'url': url_for('admin_page.page'), 'icon': ''})
            Breadcrumb.map.append({'key': 'page-contact', 'name': 'Contact Us', 
                'url': url_for('admin_page.page_contact'), 'icon': ''})
            Breadcrumb.map.append({'key': 'media', 'name': 'Media', 
                'url': url_for('admin_media.media'), 'icon': '', 'has-arg': True})
            Breadcrumb.map.append({'key': 'about', 'name': 'About Flask CMS', 
                'url': url_for('admin_main.about'), 'icon': ''})
            Breadcrumb.map.append({'key': 'comment', 'name': 'Comments', 
                'url': url_for('admin_blog.comment'), 'icon': ''})
            '''

            Breadcrumb.map.append({'key': 'message', 'name': 'Messages', 
                'url': url_for('admin_message.message'), 'icon': ''})


def set_breadcrumb(path):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            breadcrumb = []
            key = path.split()
            for k in key:
                for b in Breadcrumb.map:
                    if k == b['key']:
                        new_b = b.copy()
                        if 'has-arg' in b:
                            if b['has-arg']:
                                r = request.query_string
                                if r:
                                    r = r.decode('utf-8')
                                    new_b['url'] = new_b['url'] + '?' + r
                        breadcrumb.append(new_b)
            setattr(g, 'breadcrumb', breadcrumb)
            return f(*args, **kwargs)
        return wrapper
    return decorator
