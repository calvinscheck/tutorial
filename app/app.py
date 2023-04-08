#Importing
from flask import Flask
from . import cookies, simple_pages, orders
from app.extensions.database import db, migrate


def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')
  
  register_extensions(app)
  register_blueprints(app)

  return app

# Register the Blueprints
def register_blueprints(app: Flask):
  app.register_blueprint(cookies.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)
  app.register_blueprint(orders.routes.blueprint)

# Register the Extensions
def register_extensions(app: Flask):
  db.init_app(app)
  migrate.init_app(app, db, compare_type=True)