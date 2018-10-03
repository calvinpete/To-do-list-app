from instance.config import app_config
from flask import Flask


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config["development"])

from app.task import views
from app.account import views
