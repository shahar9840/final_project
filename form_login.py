from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo,Email


class LoginForm(FlaskForm):
    username=StringField('שם משתמש',validators=[DataRequired('הכנס שם משתמש'),Length(6,18,'שם משתמש חייב להיות בין 6-18 תווים')])
    password = PasswordField('סיסמא',validators=[DataRequired('הכנס סיסמא'),Length(6, 20,'הסיסמא חייבת להיות בין 6-20 תווים')])
    remember_me = BooleanField('זכור אותי')
    submit1=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    submit4=SubmitField('בצע הזמנה',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    submit2=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-green btn'})
    submit3=SubmitField('התחבר',render_kw={'class': 'hoverable waves-effect light-blue btn'})
