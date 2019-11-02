from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idea')
def idea():
    return render_template('idea.html', description="A project description")

@app.route('/idea-v2', methods=['POST'])
def ideaV2():
    print(request.form)
    return render_template('idea.html', description="A project description")
    
