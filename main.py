import os, random, string
from flask import Flask, render_template, redirect, request
from scripts.generate import Generator

mygen = Generator()

suggestions = []

app = Flask(__name__)

PASTES_DIR='/tmp/hackathin-pastebin' # tempfile.mkdtemp()
try:
    os.mkdir(PASTES_DIR)
except:
    pass

@app.route('/')
def index():
	global suggestions
	suggestions = []
	return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/idea', methods=['GET', 'POST'])
def idea():
	global suggestions
	tagline = mygen.generate_tagline()
	suggestions.append(tagline)
	'''suggestions_txt = ''
	for i in range(len(suggestions)):
		suggestions_txt += "Project {}:\n\t".format(i+1)
		for i in range(suggestions[0]):
			suggestions_txt += suggestions[0][i]'''
	return render_template('idea.html', tagline=tagline, suggestions=suggestions)

@app.route('/extra')
def extra():
    return render_template('extra.html')

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

@app.route('/paste', defaults = { 'name': None })
@app.route('/paste/<name>')
def paste(name=None):
    if name is None:
        return redirect('/pastes-list')
    with open(PASTES_DIR + '/' + name, 'r') as f:
        return render_template('paste.html', name=name, content=f.read())

shortlinks = {}
@app.route('/shrtn', methods=['GET', 'POST'], defaults = { 'code': None })
@app.route('/shrtn/<code>')
def shrtn(code=None):
    if request.method == 'POST':
        code = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        shortlinks[code] = request.form['link']
        return redirect('/shrtn?code=' + code)
    else:
        if code is not None and shortlinks[code] is not None:
            return redirect(shortlinks[code])
        else:
            return render_template('shrtn.html', code=request.args.get('code'))
