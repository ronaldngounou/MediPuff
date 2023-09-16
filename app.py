from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('home.html')


@app.route('/editMedication')

def edit_medication():
    return render_template('Component5.html')



if __name__ == '__main__':
    app.run(debug = True)