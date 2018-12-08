from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Ryan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'I have a headache!'
        },
        {
            'author':{'username': 'Susan'},
            'body': 'I feel better now!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)