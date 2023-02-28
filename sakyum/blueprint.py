# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask_admin.contrib.sqla import ModelView
from sakyum.utils import footer_style, template_dir, static_dir


default = Blueprint("default", __name__, template_folder=template_dir(temp_from_pkg="default_page"), static_folder=static_dir("default_style", static_from_pkg=True))
errors = Blueprint("errors", __name__, template_folder=template_dir(temp_from_pkg="default_errors"))
auth = Blueprint("auth", __name__, template_folder=template_dir(temp_from_pkg="default_page"))


def adminModelRegister(admin, reg_models, db):
  """function that will register a direct model (not model view)"""
  for reg_model in reg_models:
    admin.add_view(ModelView(reg_model, db.session))
    
"""
  the `default` blueprint above is the blueprint that we will be using for linking
  our project default pages (css, js, and favicon.ico) files and also our app default
  html pages (landing page route) that is located in your project route.py file
  `<project_name>/route.py` you will see it decorated with it ` @default.route() `.
  We also register it in the project routes.py file `reg_blueprints` list to make it accessible

  the `errors` blueprint above is for error pages, you can overite the error pages by
  defining them in your project routes.py file `<project_name>/route.py` just like the
  way we did in here down below for some of our default error pages (400, 403, 500, etc)
  by giving your desire template file path (correspond to your project templates folder)
  for each error page

  the `auth` blueprint above is for the `login, logout, register, change_password` and
  other default authentication system (route) of your project, which will let you log into admin page
"""


@errors.app_errorhandler(400)
def error_400(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('400.html', context=context), 400

@errors.app_errorhandler(401)
def error_401(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('401.html', context=context), 401

@errors.app_errorhandler(403)
def error_403(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('403.html', context=context), 403

@errors.app_errorhandler(404)
def error_404(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('404.html', context=context), 404

@errors.app_errorhandler(406)
def error_406(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('406.html', context=context), 406

@errors.app_errorhandler(415)
def error_415(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('415.html', context=context), 415

@errors.app_errorhandler(429)
def error_429(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('429.html', context=context), 429

@errors.app_errorhandler(500)
def error_500(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('500.html', context=context), 500

@errors.app_errorhandler(501)
def error_501(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('501.html', context=context), 501

@errors.app_errorhandler(502)
def error_502(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('502.html', context=context), 502

@errors.app_errorhandler(503)
def error_503(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('503.html', context=context), 503

@errors.app_errorhandler(504)
def error_504(error):
  context = {
    "head_title": "error page",
    "footer_style": footer_style,
  }
  return render_template('504.html', context=context), 504
