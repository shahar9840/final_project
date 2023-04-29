from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo,Email

class AddToCartForm(FlaskForm):
    amount = IntegerField('כמות',validators=[DataRequired('אנא הכנס כמות')])
    submit1=SubmitField('הוסף לעגלה',render_kw={'class': 'hoverable waves-effect light-blue btn'})