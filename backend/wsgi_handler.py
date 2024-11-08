# wsgi_handler.py
from app import app as flask_app
from mangum import Mangum

handler = Mangum(flask_app)