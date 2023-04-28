from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo,Email


class OrderForm(FlaskForm):
    address=StringField('כתובת',validators=[DataRequired('הכנס כתובת למשלוח')])
    comment=StringField('הערות למשלוח')
    submit1=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    submit4=SubmitField('בצע הזמנה',render_kw={'class': 'hoverable waves-effect light-blue btn'})
    submit2=SubmitField('הוסף',render_kw={'class': 'hoverable waves-effect light-green btn'})
    submit3=SubmitField('התחבר',render_kw={'class': 'hoverable waves-effect light-blue btn'})