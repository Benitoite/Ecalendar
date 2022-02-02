from flask import Flask, render_template
from datetime import date
import requests
from html.parser import HTMLParser
import requests
import numpy as np
import pandas as pd
import io
import os
import string

app= Flask(__name__)

@app.route('/el1')
def el1():
    return render_template('el1.html', hello='Hello, World!', today=date.today(), thisyear=date.today().year)
