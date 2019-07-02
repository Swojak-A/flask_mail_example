import os

from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
#Flask mail configuration  
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  
app.config['MAIL_PORT'] = 465  
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME') 
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True

# uncomment config below if you encounter problems  
# app.config['MAIL_DEBUG'] = True
# app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['TESTING'] = False
  
#instantiate the Mail class  
mail = Mail(app)  
  
#configure the Message class object and send the mail from a URL  
@app.route('/')  
def index():  
    recipient = os.getenv('MAIL_RECIPIENT')
    msg = Message('subject', sender = 'pilot.string@gmail.com', recipients=[recipient])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  



    mail.send(msg)

    return "Mail Sent"  
  
if __name__ == '__main__':
    app.run(debug = True)  
