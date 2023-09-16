from flask import Flask, render_template, request
from pyngrok import ngrok

happiness = 25
max_happiness = 50
med_names = []
med_times = []

app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('home.html')

@app.route('/EnterMedication', methods=['POST', 'GET'])

def enter_medication():
    if request.method == 'POST':
        med_name = request.form.get("submit_med")
        med_time = request.form.get("submit_time")
        
        med_names.append(med_name)
        med_times.append(med_time)
        return render_template('Component3.html')
    else:
        # Handle the GET request (or other methods) here
        return render_template('Component3.html')
    return render_template('Component3.html')

@app.route('/MainPage')

def main_page():
    return render_template('Component5.html', happiness_points = happiness)

@app.route('/Insert')
def insert():
    return render_template('Compnent.html')

if __name__ == '__main__':
    app.run(debug = True)
