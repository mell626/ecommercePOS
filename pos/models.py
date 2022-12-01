
from .ext import *
from datetime import datetime
import random


# association table for customer and order (many to many relationship)
order = db.Table('order', 
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id')),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'))

)


class Customer(db.Model):
    id  = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255))
    status = db.Column(db.Integer, default = 0)
    orders = db.relationship('Product', secondary = order, backref = 'orders')
    invoices = db.relationship('Invoice', backref = 'invoices')
    date_created = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)



    def set_password(self, pwd):
        self.password = generate_password_hash(pwd)




class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_code = db.Column(db.String(25), unique = True)    
    name = db.Column(db.String(200))
    password_hash = db.Column(db.String(400))
    designation = db.Column(db.String(50), default = 'staff')
    status = db.Column(db.String(6), default = 'false')
    date_created = db.Column(db.DateTime, default = datetime.now())


    def __init__(self, name, password_hash) -> None:
        super().__init__()
        self.user_code = 'BPOS'+ str(random.randint(0, 9999))
        self.name = name
        self.password_hash = generate_password_hash(password_hash)
        self.designation = 'staff'

    @property
    def password(self):
        raise AttributeError('cannot read object')

    def set_password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.password_hash)

    def __repr__(self) -> str:
        return f'{ self.name }'





class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300))
    product =  db.relationship('Product', backref='product_category')
    date_created = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __repr__(self) -> str:
        return f'{ self.name }'




class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(300))
    unit_price = db.Column(db.Float)
    img = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'), nullable = False)
    status = db.Column(db.String(10), default = 'inactive')
    date_created = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, code, name, unit_price, img, category_id) -> None:
        super().__init__()
        self.code = code
        self.name = name
        self.unit_price = unit_price
        self.img = img
        self.category_id = category_id

    def __repr__(self) -> str:
        return f'{ self.name }'



class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    total_amount = db.Column(db.Float)
    amount_tendered = db.Column(db.Float)
    user_id = db.Column(db.Integer) # foreign key
    sales = db.relationship('Sales', backref='sales')
    date_recorded = db.Column(db.DateTime, default = datetime.now())


    def __init__(self, total_amount, amount_tendered, user_id) -> None:
        super().__init__()
        self.total_amount = total_amount
        self.amount_tendered = amount_tendered
        



class Sales(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer) 
    unit_price = db.Column(db.Float)
    subtotal = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, quantity, unit_price, subtotal) -> None:
        super().__init__()
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = subtotal





# 


# class Sales(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     invoice_id = db.Column(db.Integer) # foreign key
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     quantity = db.Column(db.Integer) 
#     unit_price = db.Column(db.Float)
#     subtotal = db.Column(db.Float)
#     date_created = db.Column(db.DateTime, default = datetime.now())

#     def __init__(self, quantity, unit_price, subtotal) -> None:
#         super().__init__()
#         self.quantity = quantity
#         self.unit_price = unit_price
#         self.subtotal = subtotal


# class Invoice(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     customer_id = db.Column(db.Integer) # foreign key// customer id will be removed
#     total_amount = db.Column(db.Float)
#     amount_tendered = db.Column(db.Float)
#     payment_type = db.Column(db.Integer) # 0 cash, 1 bank tansfer
#     bank_account_name = db.Column(db.String(30))
#     bank_account_number = db.Column(db.String(50))
#     user_id = db.Column(db.Integer) # foreign key
#     date_recorded = db.Column(db.DateTime, default = datetime.now())

#     def __init__(self, total_amount, amount_tendered, payment_type, bank_account_name, bank_account_number) -> None:
#         super().__init__()
#         self.total_amount = total_amount
#         self.amount_tendered = amount_tendered
#         self.payment_type = payment_type
#         self.bank_account_name = bank_account_name
#         self.bank_account_number = bank_account_number


        
# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     customer_code = db.Column(db.String(40), unique = True)
#     name = db.Column(db.String(200))
#     contact_address = db.Column(db.Text)
#     date_created = db.Column(db.DateTime, default = datetime.now())

#     def __init__(self, name, contact_address) -> None:
#         super().__init__()
#         self.customer_code = 'BCC' + str(random.randint(10000, 99999))
#         self.name = name
#         self.contact_address = contact_address

#     def __repr__(self) -> str:
#         return f'{ self.name }'


# class Supplier(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     supplier_code = db.Column(db.String(40))
#     name = db.Column(db.String(300))
#     contact = db.Column(db.String(200))
#     email = db.Column(db.String(200), unique = True)
#     address = db.Column(db.Text)
#     supplies = db.relationship('ReceivedProduct', backref = 'supplier')
#     date_created = db.Column(db.DateTime, default = datetime.now())

#     def __init__(self, name, contact, email, address) -> None:
#         super().__init__()
#         self.supplier_code = 'BSC' + str(random.randint(10000,99999))
#         self.name = name
#         self.contact = contact
#         self.email = email
#         self.address = address

#     def __repr__(self) -> str:
#         return f'{ self.name }'



# class PurchaseOrder(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     product_id = db.Column(db.Integer) #foreign key
#     quantity = db.Column(db.Integer)
#     unit_price = db.Column(db.Float)
#     subtotal = db.Column(db.Float)
#     supplier_id = db.Column(db.Integer) # foreign key
#     user_id = db.Column(db.Integer) # foreign key
#     date_ordered = db.Column(db.DateTime, default = datetime.now())

#     def __init__(self, quantity, unit_price, subtotal) -> None:
#         super().__init__()
#         self.quantity = quantity
#         self.unit_price = unit_price
#         self.subtotal = subtotal

# # inventory 
# class ReceivedProduct(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
#     quantity = db.Column(db.Integer)
#     unit_price = db.Column(db.Float)
#     subtotal = db.Column(db.Float)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable = False)
#     recipient = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) 
#     date_received = db.Column(db.DateTime, default = datetime.now())


#     def __init__(self, quantity, unit_price, subtotal)  -> None:
#         super().__init__()
#         self.quantity = quantity
#         self.unit_price = unit_price
#         self.subtotal  = subtotal


