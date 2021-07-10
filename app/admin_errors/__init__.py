from flask import Blueprint

bp = Blueprint('admin_errors', __name__)

from app.admin_errors import errors
