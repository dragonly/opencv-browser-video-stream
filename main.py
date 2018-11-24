import webbrowser
import numpy as np
import cv2
from flask import Flask, render_template, make_response
app = Flask(__name__)

cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture')
def capture():
    ret, frame = cap.read()
    ret, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
    resp = make_response(buffer.tobytes())
    resp.headers['Content-Type'] = 'image/jpeg'
    resp.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return resp

webbrowser.open_new('http://localhost:5000')
