from flask_wtf import Form

from wtforms import StringField, IntegerField, TextAreaField,SubmitField, RadioField,SelectField,validators,ValidationError


class ContactForm(Form):
    name =StringField("NAme of Student ", [validators.DataRequired("Please enter your name")])

    gender= RadioField("Gender", choices=[('M','MALE'),('F','FEMALE')])
    address = StringField("ENTER ADDRESS")
    mail= StringField("ENTER MAIL",[validators.DataRequired("PLEASE ENTER YOUTR EMAIL ADDRESS")])

    age = IntegerField("AGE")

    language = SelectField("LANGUAGE", choices=[('cpp','C++'),('py','python')])

    submit = SubmitField('sent')


