import os
from flask import Flask, render_template, redirect, request
from scripts.generate import Generator

mygen = Generator()

app = Flask(__name__)

PASTES_DIR='/tmp/hackathin-pastebin' # tempfile.mkdtemp()
try:
    os.mkdir(PASTES_DIR)
except:
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idea', methods=['POST'])
def idea():
    return render_template('idea.html', tagline=mygen.generate_tagline())

@app.route('/pastes-list')
def pastes_list():
    return render_template('pastes-list.html', pastes=os.listdir(PASTES_DIR))

@app.route('/new-paste', methods=['GET', 'POST'])
def new_paste():
    if request.method == 'POST':
    	name  = request.form['name']
    	content = request.form['content']
    	with open(PASTES_DIR + '/' + name, 'w+') as f:
            f.write(content)
    	return redirect('/paste/' + str(name))
    else:
    	return render_template('new-paste.html')

@app.route('/paste/<name>')
def paste(name=None):
    if name is None:
        return redirect('/pastes-list')
    with open(PASTES_DIR + '/' + name, 'r') as f:
        return render_template('paste.html', name=name, content=f.read())
