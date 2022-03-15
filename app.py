import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
print(__name__)
UPLOAD_FOLDER = 'D://Applicationtesting//file_upload_python//'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_file():   
 return render_template('upload.html')

@app.route('/content', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        try:
            f = request.files['file']
            filename = secure_filename(f.filename)
            f.save(app.config['UPLOAD_FOLDER'] + filename)
            ##file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
            ##content = file.read()
            return render_template('display.html', content="File Uploaded Successfully") 
        except:
            return render_template('display.html', content="Failed to upload the file") 


if __name__==('__main__'):
    app.run(debug=True)
