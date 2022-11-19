


# from crypt import methods
from re import S
from .ext import *
from .models import *
from .forms import *


api = Blueprint('app_api', __name__, url_prefix='/api', template_folder='templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', }

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route('/signup', methods = ['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(form.username.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        session['user'] = form.username.data
        
        return redirect(url_for('app_api.home'))

    return render_template('signup.html', form = form)


@api.route('/login', methods = ['POST', 'GET'])
def login():

    if 'user' in session:
        flash('You are already logged in!')
        return redirect(url_for('app_api.home'))

    
    return render_template('staff.html')



@api.route('/staff-login', methods = ['GET', 'POST'])
def staff_login():
    if 'user' in session:
        return redirect(url_for('app_api.home'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        get_user = User.query.filter_by(name = login_form.username.data).first()
        
        if get_user:
            if check_password_hash( get_user.password_hash ,login_form.password.data) == True:
                session['user'] = login_form.username.data
                flash('Welcome back!')
                return redirect(url_for('app_api.home'))
            flash('Credentials not found!')
            return redirect(url_for('app_api.login'))
        flash('username incorrect!')
    
    return render_template('login.html', login_form = login_form)


@api.route('/admin-login', methods = ['POST', 'GET'])
def admin_login():
    if 'admin' in session:
        return redirect(url_for('admin.index'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password and request.method =='POST':
            if username == 'admin' and password == 'bsit@cvsu1234':
                session['admin'] = username

                return redirect(url_for('admin.index'))

    return render_template('admin-login.html')

#=================================================================================================

@api.route('/home', methods = ['POST', 'GET'])
def home():
    if 'user' in session:
        return render_template('home.html')
    return redirect(url_for('default'))

#============ POS =================================
@api.route('/pos', methods =['POST', 'GET'])
def pos():
    if 'user' in session:
        if request.method == 'POST':
            _code = request.form['pos-code']
            if _code and request.method == 'POST':
                
                product_details = Product.query.filter_by(product_code = _code).first()
                print(product_details.name)
                return redirect(url_for('app_api.pos', details = product_details.name, price = product_details.unit_price))
                    

        products = Product.query.all()
        return render_template('pos.html', products = products)
    return redirect(url_for('default'))


# @api.route('/get-item/<data>')
# def get_item(data):
#     if 'user' in session:
#         prd = Product.query.filter_by(product_code = data).first()
#         return redirect(url_for('app_api.pos', prd = prd))


@api.route('/confirm_payment', methods = ['POST'])
def confirm_payment():
    if request.method == 'POST':
        pass




#=========== Product ===============================
@api.route('/product', methods = ['POST', 'GET'])
def product():
    if 'user' in session:
        prd = Product.query.all()
        category = ProductCategory.query.all()

        return render_template('product.html', prd = prd, category = category)
    return redirect(url_for('default'))
    


@api.route('search-price', methods = ['POST'])
def search_code():
    if 'user' in session:
        pass
    return redirect(url_for('default'))



@api.route('/add-product', methods = ['POST'])
def add_product():
    if 'user' in session:
        if request.method == 'POST':
            code = request.form['code']
            name = request.form['product-name']
            product_price = request.form['product-price']
            product_img = request.files['file']
            product_category = request.form['product-category']
            
            if code and name and product_price and product_img and product_category and request.method == 'POST':
                image = ''.join(product_img.filename)
                new_product = Product(code, name, product_price, image ,product_category)
                db.session.add(new_product)
                db.session.commit()

                if 'file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)

                if product_img.filename == '':
                    flash('No selected file')
                    return redirect(request.url)

                if product_img and allowed_file(product_img.filename):
                    filename = secure_filename(product_img.filename)
                    product_img.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

                    print('success')
                    return redirect(url_for('app_api.product')) 
            print('failed')
            return redirect(url_for('app_api.product'))
    return redirect(url_for('default'))



@api.route('/delete-product', methods = ['POSt'])
def delete_product():
    pass

@api.route('/edit-product', methods = ['POST'])
def edit_product():
    pass





#===================================================
@api.route('/sales')
def sales():
    if 'user' in session:
        return render_template('sales.html')
    return redirect(url_for('default'))


@api.route('/add-sales', methods = ['POST'])
def add_sales():
    
    if request.method =='POST':
        _json = request.json
        product_code = _json['code']
        qty = _json['qty']
        subtotal = _json['subtotal']

        if product_code and qty and subtotal and request.method =='POST':
            return jsonify({'data': 'received data'})

    return redirect(url_for('default'))





# #===== INVENTORY ===================================
# @api.route('/inventory', methods = ['POST', 'GET'])
# def inventory():
#     if 'user' in session:
#         if request.method == 'POST':
#             pass


#         products = Product.query.all()
#         supplier = Supplier.query.all()
#         return render_template('inventory.html', products = products, supplier = supplier)

#     return redirect(url_for('default'))


#===================================================
@api.route('/logout')
def logout():
    session.clear()
    flash('You are logged out!')
    return redirect(url_for('default'))