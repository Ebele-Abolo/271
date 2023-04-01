import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
	username = request.form['username']
	password = request.form['password']
    width = int(request.form['width'])
    height = int(request.form['height'])

    image_file = request.file['file']
    filename = secure_file(image_file.filename)
    image_file.save(os.path.join('static/', filename))

    image = Image.open(image_file)

    image.thumbnail((width, height))

    image.save(os.path.join('static/', filename))

    return rander_template('upload.html', filename = filename)






@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()

if verufucation_chech.status == "pending":
	return "Entered OTP is wrong"
else: 
	return redirect("https://collaborative-document.onrender.com/")