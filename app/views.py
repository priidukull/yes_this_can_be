from flask import render_template, request
from app import app

from app.controller.pg_reference_processor import ParagraphReferenceProcessor
from app.forms import Form


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    query_field = Form().query_field
    query = request.form.get("query_field")
    paragraphs = ParagraphReferenceProcessor().get_referred_paragraphs(query=query)
    return render_template('index.html',
                           query_field=query_field,
                           paragraphs=paragraphs)


@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    return render_template('facebook.html')