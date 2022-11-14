from .ext import *
from .models import *


menu = Blueprint('menu', __name__, url_prefix='/menu', template_folder='templates/menu')


@menu.route('/pasta')
def pasta():    
    guest = session.get('guest')
    category = ProductCategory.query.all()
    pasta = Product.query.filter_by(category_id = 1).all()
    return render_template('pasta.html', pasta = pasta, category = category, guest = guest)

@menu.route('/chicken')
#current work
def chicken():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    chicken = Product.query.filter_by(category_id = 2).all()
    return render_template('chicken.html', chicken = chicken, category = category, guest = guest)

@menu.route('/burger')
def burger():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    burger = Product.query.filter_by(category_id = 3).all()
    return render_template('burger.html', burger = burger, category = category, guest = guest)

@menu.route('/fries')
def fries():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    fries = Product.query.filter_by(category_id = 4).all()
    return render_template('fries.html', fries = fries, category = category, guest = guest)

@menu.route('/beverage')
def beverage():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    beverage = Product.query.filter_by(category_id = 5).all()
    return render_template('beverage.html', beverage = beverage, category = category, guest = guest)

@menu.route('/dessert')
def dessert():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    dessert = Product.query.filter_by(category_id = 6).all()
    return render_template('dessert.html', dessert = dessert, category = category, guest = guest)

@menu.route('/condiment')
def condiment():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    condiment = Product.query.filter_by(category_id = 7).all()
    return render_template('condiment.html', condiment = condiment, category = category, guest = guest)

@menu.route('/hotdog')
def hotdog():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    hotdog = Product.query.filter_by(category_id = 8).all()
    return render_template('hotdog.html', hotdog = hotdog, category = category, guest = guest)

@menu.route('steak')
def steak():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    steak = Product.query.filter_by(category_id = 9).all()
    return render_template('steak.html', steak = steak, category = category, guest = guest)


@menu.route('/other')
def other():
    guest = session.get('guest')
    category = ProductCategory.query.all()
    other = Product.query.filter_by(category_id = 10).all()
    return render_template('other.html', other = other, category = category, guest = guest)