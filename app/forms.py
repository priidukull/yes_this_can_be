from flask.ext.wtf import Form
from wtforms import TextField


class Form(Form):
    text_field = TextField('tekst')