from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idea')
def idea():
    return render_template('idea.html', description="A project description")
