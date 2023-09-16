from flask import Flask, render_template

happiness = 25
max_happiness = 50

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('home.html')

@app.route('/EnterMedication')

def enter_medication():
    return render_template('Component3.html')

@app.route('/MainPage')

def main_page():
    return render_template('Component5.html', happiness_points = happiness)

if __name__ == '__main__':
    app.run(debug = True)