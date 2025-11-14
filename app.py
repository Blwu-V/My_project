from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5055))
    app.run(debug=True, port=port)