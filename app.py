from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#ADD DATA PAGE
@app.route('/add-data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'GET':
        return render_template("addData.html")
    elif request.method == 'POST':
        return render_template("addData.html")

#PRACTICE PAGE
@app.route('/practice', methods=['GET', 'POST'])
def practice():
    if request.method == 'GET':
        return render_template("practice.html")
    elif request.method == 'POST':
        return render_template("practice.html")





if __name__ == '__main__':
    app.run(debug=True)
