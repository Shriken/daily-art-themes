from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 9000, debug=True)
