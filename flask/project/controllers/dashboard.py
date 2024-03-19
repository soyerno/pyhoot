import os
from dotenv import load_dotenv
load_dotenv()

from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

# @dashboard.route('/dashboard')
# def dashboard():
#     props = {
#         "name": f'Dashboard'
#     }
#     return "dashboard"
#     # return render_template('pages/login.html', props=props)

@dashboard.route('/dashboard')
def home():
    return "dashboard"