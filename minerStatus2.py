#!/usr/bin/env python
import json
from ethermine import Ethermine
import time
import smtplib
from twilio.rest import Client

em = Ethermine()

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, "email", message)
    server.sendmail(email, "email", message)
    server.quit()

def send_sms():
    account_sid = 'account_sid'
    auth_token = 'auth_token'
    client = Client(account_sid, auth_token)

    client.messages.create(body="\n[-] WORKER(s) DOWN! PLEASE INVESTIGATE", from_='+phone_number', to='+phone_number')


def get_active_workers():
    stats = em.miner_current_stats("")
    if stats['activeWorkers'] == 2:
        print("[+] All workers online mining ether!")
    elif stats['activeWorkers'] != 2:
        send_sms()
        print("[-] Workers(s) down!")
        message = "Number of active workers is less than 2!  Please investigate..."
        send_mail("from_email", "password", message)

while True:
    get_active_workers()
    time.sleep(900)



