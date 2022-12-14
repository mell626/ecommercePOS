from .ext import *
from .models import *




ordering = Blueprint('ordering', __name__, url_prefix='/ordering', template_folder = 'templates')


s = URLSafeTimedSerializer('bsit4oc project for academic year 2022-2023')


@ordering.route('/sign-in', methods = ['GET', 'POST'])
def index():
    guest = session.get('guest')
    if 'guest' in session:
        return redirect(url_for('default', guest = guest))
    return render_template('user_signup.html')



@ordering.route('/login', methods = ['POST'])
def login():
    guest = session.get('guest')
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email and password and request.method == 'POST':
            login_customer = Customer.query.filter_by(email = email).first()

            if login_customer:
                if check_password_hash(login_customer.password, password) == True:
                    
                    session['guest'] = email
                    print('{} is logged in '.format(email))
                    return redirect(url_for('default', guest = guest))
            
                flash('incorrect email or password!')
                return redirect(url_for('ordering.index'))




@ordering.route('/signup', methods = ['POST', 'GET'])
def signup():

    if request.method == 'POST':
        email = request.form['new-email']
        password =request.form['new-password']
        last_name = request.form['last-name']
        first_name = request.form['first-name']
        middle_name = request.form.get('middle-name', None)
        contact = request.form['contact']
        address = request.form['address']

        if email and password and last_name and first_name and middle_name and contact and address and request.method == 'POST':

           token = s.dumps(email, salt = 'please-confirm-email')
           msg = Message('Confirm your email', sender = 'ramelcelada@gmail.com', recipients = [email])
           link = url_for('ordering.confirm_email', token = token, _external = True)
           msg.body = 'Click on the link to complete registration: {}'.format(link)
           mail.send(msg)

           new_customer = Customer(email, password, last_name, first_name, middle_name, contact, address)
           db.session.add(new_customer)
           db.session.commit()
        
           return 'we have sent an email confirmation'
    return redirect(url_for('ordering.index'))


@ordering.route('/confirm-email/<token>')
def confirm_email(token):
    guest = session.get('guest')
    try:
        email = s.loads(token, salt = 'please-confirm-email', max_age = 3600)
        
        user_email = Customer.query.filter_by(email = email).all()
        
        if user_email:
            db.session.commit()
            session['guest'] = email
            return redirect(url_for('default', guest = guest))
        
    except SignatureExpired:
        return 'the token is expired'

    return 'registration complete'



@ordering.route('/menu', methods =['POST', 'GET'])
def menu():
    guest = session.get('guest')

    menu = ProductCategory.query.all()
    return render_template('user_menu.html', guest = guest, menu = menu)



#current work
@ordering.route('/quantity/<name>/<price>', methods = ['POST', 'GET'])
def quantity(name, price):
    if 'guest' in session:
        guest = session.get('guest')

        #get session data to be inserted into the assoc table
        #get each order to append into the assoc table
        get_customer = Customer.query.filter_by(email = guest).first()

        return render_template('quantity.html', name = name, price = price, guest = guest, get_customer = get_customer)
    flash('Sign in to order your favorite meals.')
    return redirect(url_for('ordering.index'))


@ordering.route('/checkout', methods = ['POST'])
def checkout():
    if 'guest' in session:
        all_data = []
        if request.method == 'POST':
            data = request.get_json()

            if data and request.method == 'POST':
                try:
                    guest = session['guest']
                    #cleans the data that is passed into the query
                    new_data = [s.strip() for s in data]
                    
                    customer = Customer.query.filter_by(email = guest).first()
                    if customer:
                        #insert array of data into the association table
                        for i in new_data:
                            p = Product.query.filter_by(name = i).first()
                            customer.orders.append(p)
                            db.session.commit()

                        #attempt to bulk insert data to checkout table
                        for j in new_data:
                            c = Checkout(customer, j)
                            db.session.add(c)
                            db.session.flush()
                            db.session.commit()

                    return '<h1>sent</h1>'
                except Exception as e:
                    return 'data is not inserted'

                
                


@ordering.route('/invoice')
def invoice():
    if 'guest' in session:
        guest = session.get('guest')
        return render_template('invoice.html', guest = guest)

    return redirect(url_for('default'))




@ordering.route('/order', methods = ['GET', 'POST'])
def order():
    guest = session.get('guest')

    if 'guest' in session:
        return render_template('order.html', guest = guest) 

    return redirect(url_for('default'))