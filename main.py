import numpy as np
import cv2
from flask import Flask, make_response
app = Flask(__name__)

cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture')
def capture():
    ret, frame = cap.read()
    ret, buffer = cv2.imencode('.jpg', frame)
    resp = make_response(buffer.tobytes())
    resp.headers['Content-Type'] = 'image/jpeg'
    return resp