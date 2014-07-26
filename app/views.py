from flask import render_template, request
from app import app
from app.controller.pg_reference_processor import ParagraphReferenceProcessor
from app.forms import Form


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def render_form():
    text_field = Form().text_field
    query = request.form.get("text_field")
    paragraphs = ParagraphReferenceProcessor().get_referred_paragraphs(query=query)
    return render_template('index.html',
                           text_field=text_field,
                           paragraphs=paragraphs)
