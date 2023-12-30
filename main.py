from flask import Flask, render_template,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager,login_user,login_required,current_user,UserMixin,logout_user
from forms import SignUpForm,LoginForm,Create_Item
from datetime import datetime as dt
from random import randint
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
## CONFIGURATION SECTION 
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['FLASK_ADMIN_SWATCH'] = 'something'

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
bootstrap = Bootstrap5(app)
admin = Admin(app,template_mode='Bootstrap4')

roles = ['Customer','Admin','Supplier']

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    full_name =db.Column(db.String,nullable= False)
admin.add_view(ModelView(User,db.session))


class Items(db.Model): 
    item_id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String, nullable=False)
    item_weight = db.Column(db.Float,nullable =False)
    item_description = db.Column(db.String)
    item_image_url = db.Column(db.String)
    receiving_country = db.Column(db.String,nullable = False)
    charges_paid_on_delivery = db.Column(db.Float)
    proof_of_COD = db.Column(db.String)
    inventory_id = db.Column(db.String, nullable= False)
    scanning_date = db.Column(db.String,nullable=True)
admin.add_view(ModelView(Items,db.session))



with app.app_context():
    db.create_all()

# CONFIGURING THE LOGIN SETTINGS. 
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id): 
    return db.get_or_404(User,user_id)

## THERE SHOULD BE THE FOLLOWING PAGES TO PROJECT, 1- HOME PAGE, 2- SIGN-UP PAGE, 3- SIGN-IN PAGE, 4-GET ALL SCANNED PRODUCTS PER USER, 5- DASHBOARD

# HOME PAGE
@app.route('/')
def home(): 
    return render_template('index.html')

# SIGNUP PAGE
@app.route('/signup', methods = ['GET','POST'])
def signup(): 
    sign_up_form = SignUpForm()
    if sign_up_form.validate_on_submit():
      
        new_user = User(
            username = sign_up_form.username.data,
            password = generate_password_hash(sign_up_form.password.data,method = 'pbkdf2',salt_length=6),
            full_name= sign_up_form.full_name.data
            )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('dashboard'))
    return render_template('signup.html', form = sign_up_form)

# # SIGNIN PAGE
@app.route('/login',methods=['GET','POST'])
def login(): 
    login_form = LoginForm()
    if login_form.validate_on_submit():
        enterd_password = login_form.password.data
        user = db.session.execute(db.select(User).where(User.username==login_form.username.data)).scalar()
        if check_password_hash(user.password,enterd_password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html',form = login_form)

# SIGNOUT PAGE
@app.route('/logout')
def logout(): 
    logout_user()
    return redirect(url_for('home'))

# DASHBOARD
@app.route('/dashboard')
@login_required
def dashboard(): 

    db.session.execute(db.select(Items).where(Items.inventory_id==current_user.username)).scalar()

    return render_template('admin.html',)



@app.route('/add_item',methods = ['GET','POST'])
def new_item(): 
    add_item = Create_Item()
    if add_item.validate_on_submit():
        new_item = Items(
            tracking_number = add_item.tracking_number.data,
            item_weight = add_item.item_weight.data,
            item_description = add_item.item_description.data,
            item_image_url = add_item.item_image_url.data,
            receiving_country = add_item.receiving_country.data,
            charges_paid_on_delivery = add_item.charges_paid_on_delivery.data,
            proof_of_COD = add_item.proof_of_COD.data,
            inventory_id = add_item.inventory_id.data,
            scanning_date = str(dt.today())
            )

        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    return render_template('new_item.html',form = add_item)



if __name__ == "__main__": 
    app.run(debug=True)