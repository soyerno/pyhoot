import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

page_name = os.environ.get('NAME')
company_name = os.environ.get('NAME')
base_props = {
        "company": f'{page_name}',
        "year": datetime.now().year
}

@main.route("/")
def home():
    props = {
        "name": f'{page_name}'
    }
    props.update(base_props)
    return render_template('pages/home.html', props=props)