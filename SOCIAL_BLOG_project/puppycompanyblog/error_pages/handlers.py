from flask import Blueprint, render_template
error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404)#not a basic routing instead connect app_a general error handler
def error_404(error):#view
    return render_template('error_pages/404.html'), 404 #returning atuple where the first part is render_template

@error_pages.app_errorhandler(403)#forbidden acces
def error_403(error):
    return render_template('error_pages/403.html'), 403