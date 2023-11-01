from flask import Flask, render_template, request
from classifer import *

app = Flask(__name__)
@app.route('/', methods=['GET'])
def breast_cancer():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    classification = detection(image_path)
    return render_template('index.html', prediction=classification, image_path='.'+image_path)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
