#!/usr/bin/python3

from flask import Flask, render_template, request, json, jsonify
import datetime as dt
import numpy as np
from scipy import stats

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Linear Regression API!'


@app.route('/api', methods=['POST'])
def api():
    if not request.is_json:
        x_raw = request.form['x'].strip()
        y_raw = request.form['y'].strip()

    else:
        req_data = request.get_json()
        x_raw = req_data['x'].strip()
        y_raw = req_data['y'].strip()

    x = np.array(x_raw.split(","),dtype=np.float32)
    y = np.array(y_raw.split(","),dtype=np.float32)
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

    return('\n'.join(['y = mx + b',
                      'm = %s',
                      'b = %s',
                      'r_value: %s',
                      'p_value: %s',
                      'std_err: %s']) % (slope,intercept,r_value,p_value,std_err))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)