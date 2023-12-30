from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,URLField,FloatField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    username = StringField('User Name',validators=[DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    submit = SubmitField('Submit',validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('User Name',validators=[DataRequired()])
    password = PasswordField('Password', validators= [DataRequired()])
    submit = SubmitField('Submit',validators=[DataRequired()])


class Create_Item(FlaskForm): 
    # (!) Get back here later, What will you do in case of Bulk & Quantity... 
    tracking_number = StringField('Tracking Number',validators=[DataRequired()])
    item_weight = FloatField('Item Weight',validators=[DataRequired()]) 
    item_description = StringField('Item Description',validators=[DataRequired()])
    item_image_url = URLField('Item Image') # CONSIDER CHANGING THIS, WITH UPLOADING.
    receiving_country= StringField('Receiving Country',validators=[DataRequired()])
    charges_paid_on_delivery = FloatField('Amount Paid On Delivery')
    proof_of_COD = URLField('Proof of COD') # CONSIDER CHANGING THIS, WITH UPLOADING.
    inventory_id = StringField('Inventory ID', validators=[DataRequired()])
    submit = SubmitField("Submit Item",validators=[DataRequired()])