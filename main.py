
from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap5
from wtforms import StringField,EmailField,SubmitField
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from twilio.rest import Client

import os
from dotenv import load_dotenv

load_dotenv()

class Message(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email=EmailField("Email",validators=[DataRequired()])
    message=CKEditorField("Message",validators=[DataRequired()])
    submit=SubmitField("Send!")


account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
num=os.environ.get("num")
tonum=os.environ.get("tonum")

app=Flask(__name__)
FLASK_KEY=os.environ.get("FLASK_KEY")
app.config['SECRET_KEY'] = FLASK_KEY
Bootstrap5(app)
ckeditor=CKEditor(app)


@app.route('/')
def portfolio():
    return render_template('index.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
   message_form=Message()
   if message_form.validate_on_submit():
    print(message_form.name.data,message_form.message.data)
    
    cilent=Client(account_sid,auth_token)
    message=cilent.messages.create(
        from_=f"{num}",
        to=f"{tonum}",
        body=f"Subject:Portfolio Message\n\nFrom:{message_form.name.data}\nMail:{message_form.email.data}\nMessage:{message_form.message.data}"
        )
    print(message.status)
    print(message.body)
    return render_template('contact.html',sent=True)
    
   return render_template('contact.html',form=message_form)
   
    # return "<h1>Hi</h1>"



if __name__=='__main__':
    app.run(debug=True)