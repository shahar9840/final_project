from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,BooleanField,PasswordField,ValidationError
from wtforms.validators import DataRequired,Length,EqualTo,Email


class CreateCategoryForm(FlaskForm):
    create_category = StringField('שם קטגוריה',validators=[ DataRequired('הכנס שם לקטגוריה')])
    imageUrl = StringField('כתובת תמונה',validators=[DataRequired('הכנס כתובת תמונה')])
    submit1=SubmitField('הוסף',render_kw={'class': 'waves-effect light-blue btn'})
    submit4=SubmitField('בצע הזמנה',render_kw={'class': 'waves-effect light-blue btn'})
    submit2=SubmitField('הוסף',render_kw={'class': 'waves-effect light-green btn'})
    submit3=SubmitField('התחבר',render_kw={'class': 'waves-effect light-blue btn'})