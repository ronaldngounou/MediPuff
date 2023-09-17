from flask import Flask, render_template, request
from pyngrok import ngrok
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

med_names = []
med_times = []
phone_number = 0000000000

#stuff to send text messages
# Your Account SID from twilio.com/console
account_sid = "AC1301b04dcb50efa82ad50164c3c4eb9e"
# Your Auth Token from twilio.com/console
auth_token  = "4fc352e00cd88bd406f3a0c88eae887f"
client = Client(account_sid, auth_token)


app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template('home.html')

@app.route('/EnterMedication', methods=['POST', 'GET'])

def enter_medication():
    if request.method == 'POST':
        med_name = request.form.get("submit_med")
        med_time = request.form.get("submit_time")
        phone_number = request.form.get("phone_number")
        
        med_names.append(med_name)
        med_times.append(med_time)
        
        #message = client.messages.create(
         #   to="{}{}".format("+", phone_number), 
          #  from_="+18445610671",
           # body="You have set up your text notifications!")
        
       
        #print(message.sid)
        return render_template('Component3.html')
    else:
        # Handle the GET request (or other methods) here
        return render_template('Component3.html')
    return render_template('Component3.html')

@app.route('/MainPage', methods=["POST", "GET"])

def main_page():
    if request.method == 'POST':
        return render_template('Component5.html', items = med_names)
    else:
        return render_template('Component5.html', items = med_names)

@app.route('/Insert')
def insert():
    return render_template('Compnent.html')



if __name__ == '__main__':
    app.run(debug = True)
