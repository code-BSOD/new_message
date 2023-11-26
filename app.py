from flask import Flask, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, EmailField
from wtforms.validators import DataRequired, Regexp, Email
import email_validator
import uuid
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = 'mysecretKey2894'

current_dir = os.getcwd()

class MessageForm(FlaskForm):
    # email = StringField("Enter your email address: ", validators=[DataRequired(), Regexp(r"^[-\w\.\+]+@([-\w]+\.)+[-\w\ ]{2,4}$")])
    email = EmailField(validators=[Email("Enter a valid Email:)"), DataRequired()])
    name = StringField("Enter your name: ", validators=[DataRequired()])
    # email = EmailField(validators=[email_validator, DataRequired()])
    message = TextAreaField("Enter your message: ")
    submit = SubmitField("Send :)")

@app.route("/", methods=['GET', 'POST'])
def index():
    form = MessageForm()
    email = ''
    message = """"""
    name = ''


    if form.validate_on_submit():
        session['email'] = form.email.data
        session['message'] = form.message.data
        session['name'] = form.name.data

        user_data = [session['email'], session['name'], session['message']]
        
        
        filename = str(uuid.uuid4())

        with open(f"{filename}.txt", 'w') as output:
            output.write(str(user_data))


        return redirect(url_for("thank_you"))
    
    
    return render_template("message.html", form=form, email=email, message=message)


@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    # app.run(host="0.0.0.0", port=8080)