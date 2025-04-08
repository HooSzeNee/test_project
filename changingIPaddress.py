from flask import Flask, render_template
import git

app = Flask(__name__) 
# app.config['SERVER_NAME'] = 'guiding-cub-tight.ngrok-free.app'
# app.config['APPLICATION_ROOT'] = '/'

git remote add origin https://github.com/HooSzeNee/test_project.git
git branch -M main
git push -u origin main

@app.route('/')
def index():
    return render_template('example.html')

if __name__ == '__main__': 
	app.run(host = '0.0.0.0') 
