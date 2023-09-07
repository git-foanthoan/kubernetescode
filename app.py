from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Asher happy birthday and please like and share out video.!!!'
