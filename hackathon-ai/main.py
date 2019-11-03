import os, random, string
from flask import Flask, render_template, redirect, request
from scripts.generate import Generator
import logging
import logstash
import sys

mygen = Generator()

app = Flask(__name__)


# Set up logging
host = 'localhost'
logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))
typeTagLine = ''

PASTES_DIR='/tmp/hackathin-pastebin' # tempfile.mkdtemp()
try:
    os.mkdir(PASTES_DIR)
except:
    pass

@app.route('/')
def index():
    global typeTagLine
    typeTagLine = ''
    logger.info('python-logstash: Index page requested')
    return render_template('index.html')

@app.route('/about')
def about():
    logger.info('python-logstash: About page requested')
    return render_template('about.html')

@app.route('/idea', methods=['GET', 'POST'])
def idea():
    logger.info('python-logstash: Index page requested')
    typeTagLine = ''
    if request.method == 'POST':
        typeTagLine = request.form['Topic']
    return render_template('idea.html', tagline=mygen.generate_tagline(), topic=typeTagLine)

@app.route('/extra')
def extra():
    logger.info('python-logstash: Extra page requested')
    return render_template('extra.html')

@app.route('/pastes-list')
def pastes_list():
    logger.info('python-logstash: Index page requested')
    return render_template('pastes-list.html', pastes=os.listdir(PASTES_DIR))

@app.route('/new-paste', methods=['GET', 'POST'])
def new_paste():
    logger.info('python-logstash: New paste requested')
    if request.method == 'POST':
    	name  = request.form['name']
    	content = request.form['content']
    	with open(PASTES_DIR + '/' + name, 'w+') as f:
            f.write(content)
            logger.info('python-logstash: New paste created')
    	return redirect('/paste/' + str(name))
    else:
    	return render_template('new-paste.html')

@app.route('/paste', defaults = { 'name': None })
@app.route('/paste/<name>')
def paste(name=None):
    logger.info('python-logstash: Pastebin page requested')
    if name is None:
        return redirect('/pastes-list')
    with open(PASTES_DIR + '/' + name, 'r') as f:
        return render_template('paste.html', name=name, content=f.read())

shortlinks = {}
@app.route('/shrtn', methods=['GET', 'POST'], defaults = { 'code': None })
@app.route('/shrtn/<code>')
def shrtn(code=None):
    logger.Info('python-logstash: linkshorten page requested')
    if request.method == 'POST':
        code = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        shortlinks[code] = request.form['link']
        return redirect('/shrtn?code=' + code)
    else:
        if code is not None and shortlinks[code] is not None:
            return redirect(shortlinks[code])
        else:
            return render_template('shrtn.html', code=request.args.get('code'))

@app.route('/todo')
def todo():
    return render_template('todo.html')
