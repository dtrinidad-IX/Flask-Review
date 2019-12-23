from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config["SECRET_KEY"] = "KJDnvknjqjk13k4j*&kn"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'



from main import routes
