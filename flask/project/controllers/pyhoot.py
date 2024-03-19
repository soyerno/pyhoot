import os
from dotenv import load_dotenv
load_dotenv()

from flask import Blueprint, render_template

pyhoot = Blueprint('pyhoot', __name__)

# @pyhoot.route('/dashboard')
# def dashboard():
#     props = {
#         "name": f'Dashboard'
#     }
#     return "dashboard"
#     # return render_template('pages/login.html', props=props)

@pyhoot.route('/dashboard/pyhoot/create')
def create():
    props = {}
    return render_template('pages/pyhoot/create.html', props=props)

@pyhoot.route('/dashboard/pyhoot/create', methods=['POST'])
def new():
    return "SAVED"

@pyhoot.route('/dashboard/pyhoot/:id')
def view():
    return f"view ${id}"

@pyhoot.route('/dashboard/pyhoot/:id', methods=['PUT'])
def update():
    return "UPDATED"

@pyhoot.route('/dashboard/pyhoot/:id', methods=['DELETE'])
def delete():
    return "DELETED"