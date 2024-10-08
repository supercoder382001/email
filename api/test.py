import random
import smtplib
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/emailverify', methods=['POST'])
def email_verification():
    res = request.get_json()
    email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]
    count = 0
    receiver_email = res.get('email')
    for domain in email_check1:
        if domain in receiver_email:
            count += 1
    for site in email_check2:
        if site in receiver_email:
            count += 1

    if "@" not in receiver_email or count != 2:
        responsed = {
            "message": "invalid email id",
            "code": 103
        }
        return json.dumps(responsed)

    responsed = {
        "message": "verified",
        "code": 101
    }
    return json.dumps(responsed)


@app.route('/sendotp', methods=['POST'])
def otp():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    new_otp = random.randint(100000, 999999)
    res = request.get_json()
    emailed = res.get('email')
    password = "icrjkrmrzmfhkalr"
    server.login("jatindua2001@gmail.com", password)
    body = "Dear" + "," + "\n" + "\n" + "your OTP is " + str(new_otp) + "."
    subject = "OTP verification using python"
    message = f'subject:{subject}\n\n{body}'
    server.sendmail("jatindua2001@gmail.com", emailed, message)
    responsed = {
        "message": "Otp has been Sent to your email id",
        "code": 101
    }
    server.quit()
    return json.dumps(responsed)
