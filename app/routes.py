from app import app
from flask import render_template

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	posts = ['test1', 'test2', 'test3']
	return render_template('index.html', title='', posts=posts)

@app.route('/about_me', methods=['GET'])
def about_me():
	return 'About me page'

@app.route('/login', methods=['GET', 'POST'])
def login():
	return 'login page'

@app.route('/logout')
def logout():
	return 'logout user'

