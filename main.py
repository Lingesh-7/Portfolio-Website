
from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap5
from wtforms import StringField,EmailField,SubmitField
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
import smtplib

import os
from dotenv import load_dotenv

load_dotenv()

class Message(FlaskForm):
    name=StringField("Name",validators=[DataRequired()])
    email=EmailField("Email",validators=[DataRequired()])
    message=CKEditorField("Message",validators=[DataRequired()])
    submit=SubmitField("Send!")

EMAIL_KEY=os.environ.get("EMAIL_KEY")
PASSWORD_KEY=os.environ.get("PASSWORD_KEY")
TO_MAIL_ADDRESS=os.environ.get("TO_MAIL_ADDRESS")

app=Flask(__name__)
FLASK_KEY=os.environ.get("FLASK_KEY")
app.config['SECRET_KEY'] = FLASK_KEY
Bootstrap5(app)
ckeditor=CKEditor(app)

projects={'Box office model':{'repo':'https://github.com/Lingesh-7/Box-Office-Model.git','color':'danger'},
'My Blog Website':{'repo':'https://github.com/Lingesh-7/MY-BLOG-WEBSITE.git','color':'warning'},
'Twitter-News-Bot':{'repo':'https://github.com/Lingesh-7/Twitter-News-Bot-for-Puducherry.git','color':'info'},
'PDF TO Audio\nconverter':{'repo':'https://github.com/Lingesh-7/PDF-TO-Audio-converter.git','color':'light'},

'Real Estate Model':{'repo':'https://github.com/Lingesh-7/Real-Estate-Model.git','color':'danger'},
'Cafe Website':{'repo':'https://github.com/Lingesh-7/Cafe-Website-with-API.git','color':'warning'},
'Job application Bot':{'repo':'https://github.com/Lingesh-7/Job-application-Bot.git','color':'info'},
'Snake-Game':{'repo':'https://github.com/Lingesh-7/Snake-Game.git','color':'light'},

'Dr Semmelweis Analysis':{'repo':'https://github.com/Lingesh-7/Dr-Semmelweis-Analysis.git','color':'danger'},
'Image Color Pallete':{'repo':'https://github.com/Lingesh-7/Image-Color-Pallete.git','color':'warning'},
'Flipkart scraping':{'repo':'https://github.com/Lingesh-7/Flipkart-scraping-and-data-enrty.git','color':'info'},
'Password manager':{'repo':'https://github.com/Lingesh-7/Advance-Password-manager.git','color':'light'},


'Nobel Prize Analysis':{'repo':'https://github.com/Lingesh-7/Nobel-Prize-Analysis.git','color':'danger'},
'Top 10 Movies':{'repo':'https://github.com/Lingesh-7/Top-10-Movies.git','color':'warning'},
'Quiz App':{'repo':'https://github.com/Lingesh-7/Advance-Quiz-App.git','color':'info'},
'Rain Alert':{'repo':'https://github.com/Lingesh-7/Rain-Alert.git','color':'light'},

}
@app.route('/')
def portfolio():
    return render_template('index.html', project=projects)

@app.route('/contact',methods=['GET','POST'])
def contact():
   message_form=Message()
   if message_form.validate_on_submit():
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_KEY,password=PASSWORD_KEY)
        connection.sendmail(from_addr=EMAIL_KEY,
                            to_addrs=TO_MAIL_ADDRESS,
                            msg=f"Subject:Portfolio Message\n\nFrom:{message_form.name.data}\nMail:{message_form.email.data}\nMessage:{message_form.message.data}")
        # return redirect(url_for('portfolio'))
        return render_template('contact.html',sent=True)
    
   return render_template('contact.html',form=message_form)
   
    # return "<h1>Hi</h1>"



if __name__=='__main__':
    app.run(debug=True)