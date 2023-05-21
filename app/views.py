from flask import render_template
from app import create_app

views_blueprint = Blueprint('views', __name__)

@app.route('/')
def home():
    return render_template('home.html')
