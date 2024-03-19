from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

from flask_socketio import SocketIO
# socketio = SocketIO(logger=True, engineio_logger=True)
socketio = SocketIO()

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        static_url_path='', 
        static_folder='client/public',
        template_folder='templates'
    )

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    socketio.init_app(app)
    db.init_app(app)

    #LOGIN MANAGER CONFIG
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    # ENDS LOGIN MANAGER CONFIG

    # register models
    from .models import User, Pyhoot

    with app.app_context():
        db.create_all()

        # db.session.add(User('admin', 'admin@example.com', '1234'))
        # db.session.add(User('guest', 'guest@example.com', '1234'))
        # db.session.add(Pyhoot('test1', 1, {'duration': 10000}, {'questions': [{'title': "¿Que version de python usamos?", 'answers': [1, 2,3,4]}]}))
        db.session.commit()
        
        # users = User.query.all()
        # print(users)
    
    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # dashboard for auth parts of app
    from .controllers.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from .controllers.socket import socket as socket_blueprint
    app.register_blueprint(socket_blueprint)

    from .controllers.pyhoot import pyhoot as pyhoot_blueprint
    app.register_blueprint(pyhoot_blueprint)

    return app