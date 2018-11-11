#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from countries import query_api, query_api_all
import math
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
	data = []
	error = None
	resp = query_api_all()
	if resp:
	   data.append(resp)
	if len(data) != 2:
		error = 'Bad Response from Countries API'
	return render_template(
		'countries.html',
		data=data[0],
		error=error)
@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Countries API'
    return render_template(
        'result.html',
        data=data,
        error=error)
if __name__=='__main__':
    app.run(debug=True)