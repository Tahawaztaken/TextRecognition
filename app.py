from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#ADD DATA PAGE
@app.route('/add-data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'GET':
        return ""
    elif request.method == 'POST':
        return "2"

#PRACTICE PAGE
@app.route('/practice', methods=['GET', 'POST'])
def practice():
    if request.method == 'GET':
        return ""
    elif request.method == 'POST':
        return "2"





if __name__ == '__main__':
    app.run(debug=True)
