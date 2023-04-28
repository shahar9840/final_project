import re
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo,Email





    

class SignUpForm(FlaskForm):
    first_name = StringField('שם פרטי',validators=[DataRequired('הכנס שם פרטי')])
    last_name =StringField('שם משפחה',validators=[DataRequired('הכנס שם משפחה')]) 
    username=StringField('שם משתמש',validators=[DataRequired('הכנס שם משתמש'),Length(6,18,'שם משתמש חייב להיות בין 6-18 תווים')])
    email = StringField('אמייל',validators=[DataRequired('הכנס אימייל'),Email('הכנס כתובת אימייל תקינה')])
    password = PasswordField('סיסמא',validators=[DataRequired('הכנס סיסמא'),Length(6, 20,'הסיסמא חייבת להיות בין 6-20 תווים')])
    confirm_password = PasswordField('אישור סיסמא',validators=[EqualTo('password','הסיסמא חייבת להיות תואמת')])
    
    submit1=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    submit4=SubmitField('בצע הזמנה',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    submit2=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-green btn'})
    submit3=SubmitField('התחבר',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    address=StringField('כתובת')
    
    
    def validate_password(self, field):
        password = field.data
        if not re.search(r'[A-Z]',password):
            raise ValidationError('הסיסמא חייבת לכלול לפחות תו גדול אחד')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
            raise ValidationError('הסיסמא חייבת לכלול לפחות תו מיוחד אחד')
    






    
# class Form(FlaskForm):
#     first_name = StringField('שם פרטי',validators=[
#         DataRequired('הכנס שם פרטי')
#         ])
#     last_name =StringField('שם משפחה',validators=[
#         DataRequired('הכנס שם משפחה')
#         ]) 
#     username=StringField('שם משתמש',validators=[DataRequired('הכנס שם משתמש'),Length(6,18,'שם משתמש חייב להיות בין 6-18 תווים')])
#     email = StringField('אמייל',validators=[DataRequired('הכנס אימייל'),Email('הכנס כתובת אימייל תקינה')])
#     password = PasswordField('סיסמא',validators=[DataRequired('הכנס סיסמא'),Length(6, 20,'הסיסמא חייבת להיות בין 6-20 תווים')])
#     confirm_password = PasswordField('אישור סיסמא',validators=[EqualTo('password','הסיסמא חייבת להיות תואמת')])
#     remember_me = BooleanField('זכור אותי')
#     submit1=SubmitField('הוסף',render_kw={'class': 'waves-effect light-blue btn'})
#     submit2=SubmitField('הוסף',render_kw={'class': 'waves-effect light-green btn'})
#     submit3=SubmitField('התחבר',render_kw={'class': 'waves-effect light-blue btn'})
#     create_category = StringField('שם קטגוריה')
#     imageUrl = StringField('כתובת תמונה')
#     dish_name= StringField('שם מנה',validators=[
#         DataRequired('Please enter your Dish Name'),
#         Length(2,100,'name has to be up to 2 digit')
#         ])
#     price = IntegerField('מחיר',validators=[DataRequired('Please Enter Price')])
#     description = StringField('תיאור')
#     is_gluten_free= BooleanField('ללא גלוטן')
#     is_vegeterian = BooleanField('טבעוני')
    
    
#     def validate_password(self, field):
#         password = field.data
#         if not re.search(r'[A-Z]',password):
#             raise ValidationError('הסיסמא חייבת לכלול לפחות תו גדול אחד')
#         if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
#             raise ValidationError('הסיסמא חייבת לכלול לפחות תו מיוחד אחד')