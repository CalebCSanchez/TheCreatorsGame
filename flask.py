import random
import string
from flask import FLask, render_template, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/chapter1')
def chapter_one():
	return render_template('chapter_one.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0', port=8080)
