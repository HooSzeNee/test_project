from flask import Flask, render_template

app = Flask(__name__) 
# app.config['SERVER_NAME'] = 'guiding-cub-tight.ngrok-free.app'
# app.config['APPLICATION_ROOT'] = '/'

@app.route('/')
def index():
    return render_template('example.html')

if __name__ == '__main__': 
	app.run(host = '0.0.0.0') 
