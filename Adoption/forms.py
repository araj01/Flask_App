#form classes

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm): #inherit from flaskform
    name = StringField('Name of puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField("Id number of puppy to remove: ")
    submit = SubmitField('Remove Puppy')

class OwnerForm(FlaskForm):
    name = StringField('Name of Owner: ')
    id = IntegerField('Id of puppy: ')
    submit = SubmitField('Add Owner')
