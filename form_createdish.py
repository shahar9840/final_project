from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo,Email

class CreateDishForm(FlaskForm):
    dish_name= StringField('שם מנה',validators=[ DataRequired('הכנס שם למנה')])
    price = IntegerField('מחיר',validators=[DataRequired('הכנס מחיר למנה')])
    imageUrl = StringField('כתובת תמונה',validators=[DataRequired('הכנס כתובת תמונה')])
    description = StringField('תיאור')
    is_gluten_free= BooleanField('ללא גלוטן')
    is_vegeterian = BooleanField('טבעוני')
    submit2=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-green btn'})
