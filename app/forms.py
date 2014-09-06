from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField


class Form(Form):
    text_field = TextField('tekst')
    query_field = TextAreaField('query_field')