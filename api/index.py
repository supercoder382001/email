import random
import smtplib
import json
from flask import Flask, request
import requests

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello! World'

@app.route('/verify', methods=['POST'])
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

@app.route('/verifyotp',methods=['POST'])
def verify():
    res=request.get_json()
    email=res.get('email')
    otp=res.get('otp')
    responsed = {
        "message": "OTP Verified",
        "code": 101
    }
    return json.dumps(responsed)

@app.route('/resendotp',methods=['POST'])
def resend():
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

@app.route('/verifyemail',methods=['POST'])
def emailverify():
    res=request.get_json()
    email=res.get('email')
    url = 'https://zmvjylvafmgqpxqtrblc.supabase.co/rest/v1/rpc/CheckUser'
    data = { "email": email }
    headers = {
        "Content-Type": "application/json",
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inptdmp5bHZhZm1ncXB4cXRyYmxjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM0ODk4MTIsImV4cCI6MjAzOTA2NTgxMn0.-qK5cu9zPoVtcpGAf14-XuJ55SMYXpfpXXgp6lz-Z4M",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inptdmp5bHZhZm1ncXB4cXRyYmxjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjM0ODk4MTIsImV4cCI6MjAzOTA2NTgxMn0.-qK5cu9zPoVtcpGAf14-XuJ55SMYXpfpXXgp6lz-Z4M"
    }
    response=requests.post(url,json=data, headers=headers)
    return(response.content)
