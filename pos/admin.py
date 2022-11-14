from .ext import *
from .models import *



class AdminHomeView(AdminIndexView):
    
    def is_accessible(self):
        if 'admin' in session:
            return True
        return False


class CustomerView(ModelView):
    can_create = False
    can_edit = True
    can_delete = False
    can_export = True

    column_exclude_list = ['password', ]
    column_searchable_list = ['email']

    def is_accessible(self):
        if 'admin' in session:
            return True        
        return False


class UserView(ModelView):
    can_create =False
    can_edit =True
    can_delete = True
    can_export = True

    column_exclude_list =['password_hash',]


    def is_accessible(self):
        if 'admin' in session:
            return True
        return False


class CategoryView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True

    form_excluded_columns = ['date_created', 'product']

    def is_accessible(self):
        if 'admin' in session:
            return True
        return False 



class ProductView(ModelView):
    can_create = False
    can_edit = True
    can_delete = True
    can_export = True

    def is_accessible(self):
        if 'admin' in session:
            return True
        return False 


admin = Admin(name= 'POS online', template_mode= 'bootstrap3', index_view=AdminHomeView())



admin.add_view(CustomerView(Customer, db.session))
admin.add_view(UserView(User, db.session))
admin.add_view(CategoryView(ProductCategory, db.session))
admin.add_view(ProductView(Product, db.session))



# class UserView(ModelView):
#     can_create =False
#     can_delete = False
#     can_edit = True
#     can_export = True
#     column_exclude_list = ['password_hash', ]
#     column_searchable_list = ['name',]
#     create_modal = True
#     edit_modal = True

#     def is_accessible(self):
#         if 'user' in session:
#             return True         
#         return False



# class ProductView(ModelView):
#     can_create =True
#     can_delete = True
#     can_edit = True 
#     can_export = True

#     column_searchable_list = ['name', 'product_code', ]
#     # create_modal = True
#     # edit_modal = True
#     form_excluded_columns = ['date_created', 'product_code']



# class ProductCategoryView(ModelView):
#     can_create = True
#     can_delete = True
#     can_edit = True
#     can_export = True

#     create_modal = True
#     edit_modal = True

#     form_excluded_columns = [ 'product' ,'code']


# class ReceivedProductView(ModelView):
#     can_create = False
#     can_delete = True
#     can_edit = True
#     can_export = True

#     create_modal = True
#     edit_modal = True
#     form_excluded_columns = ['date_received',]


# class SalesView(ModelView):
#     can_create = False
#     can_delete = False
#     can_edit = False
#     can_export = True


# class SupplierView(ModelView):
#     can_create = True
#     can_delete = True
#     can_edit = True
#     can_export = True
#     form_excluded_columns = ['date_created', 'supplies',]


# admin.add_view(UserView(User, db.session))
# admin.add_view(ProductView(Product, db.session))
# admin.add_view(ProductCategoryView(ProductCategory, db.session))
# admin.add_view(ReceivedProductView(ReceivedProduct, db.session))
# admin.add_view(SalesView(Sales, db.session))
# admin.add_view(SupplierView(Supplier, db.session))