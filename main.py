from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, flash, url_for
from predict import get_prediction
import os


model = load_model('model')
UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html', image_segmented=None, real_image=None)
    elif request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            print("full path is ", filename)
            url_for_mask = get_prediction(model, os.path.join(app.config['UPLOAD_FOLDER'],filename))
            print("image_segmented is True")
            return render_template('index.html', image_segmented=url_for_mask, real_image=filename)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

