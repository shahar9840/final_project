from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SelectMultipleField,TextAreaField,SubmitField,RadioField,BooleanField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,Email




    

class Form(FlaskForm):
    first_name = StringField('First Name',validators=[
        DataRequired('Please enter your First Name'),
        Length(min=2,max=100)
        ])
    last_name =StringField('Last Name',validators=[
        DataRequired('Please enter your Last Name'),
        Length(min=2,max=100)
        ]) 
    username=StringField('Username',validators=[DataRequired('Please enter Username')])
    email = StringField('Email',validators=[DataRequired('Please enter Email'),Email('Please enter vaild Email')])
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password',validators=[EqualTo('password','Password must Match')])
    remember_me = BooleanField('Remember Me')
    submit1=SubmitField('Send',render_kw={'class': 'waves-effect light-blue btn'})
    submit2=SubmitField('Send',render_kw={'class': 'waves-effect light-green btn'})
    create_category = StringField('Category Name')
    imageUrl = StringField('Insert Image Url')


