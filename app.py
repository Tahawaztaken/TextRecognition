from flask import Flask, request, render_template, redirect, url_for, session
from bidict import bidict
from random import choice
import numpy as np

app = Flask(__name__)
app.secret_key = 'superdupersafekey'

ENCODER = bidict({
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
})

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")



#ADD DATA PAGE
@app.route('/add-data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'GET':
        response_message = session.get('response_message', '')
        random_letter = choice(list(ENCODER.keys()))
        return render_template("addData.html", letter=random_letter, response_message=response_message)
    elif request.method == 'POST':
        label = request.form['letter']
        labels = np.load("data/labels.npy")
        labels = np.append(labels, label)
        np.save("data/labels.npy", labels)

        pixels = request.form['pixels']
        pixels = pixels.split(',')
        img = np.array(pixels).astype(float).reshape(1, 50, 50)
        imgs = np.load("data/images.npy")
        imgs = np.vstack([imgs, img])
        np.save("data/images.npy", imgs)

        session['response_message'] = f"[{label}] was added to the training dataset."
        return redirect(url_for('add_data'))

#PRACTICE PAGE
@app.route('/practice', methods=['GET', 'POST'])
def practice():
    if request.method == 'GET':
        return render_template("practice.html")
    elif request.method == 'POST':
        return render_template("practice.html")





if __name__ == '__main__':
    app.run(debug=True)
