from .ext import *
from .models import *
from .admin import *
from .api import api
from .ordering import *
from .menu import *


def create_app():
    app = Flask(__name__)

    UPLOAD_FOLDER = 'pos\\static\\img'


    app.config['SECRET_KEY'] ='dfavbsfgnbsrvDBSNBFCAwdW32R3FER'
    app.config['WTF_CSRF_SECRET_KEY'] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_USERNAME'] = 'ramelcelada@gmail.com'
    app.config['MAIL_PASSWORD'] = 'dfvxobsmvoubeymq'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USE_TLS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    

    app.register_blueprint(api)
    app.register_blueprint(ordering)
    app.register_blueprint(menu)

    db.init_app(app)
    admin.init_app(app)
    mail.init_app(app)

    @app.route('/')
    def default():
        guest = session.get('guest')
        return render_template('index.html', guest = guest)


    @app.before_first_request
    def init_db():
        db.create_all()

        


    return app
