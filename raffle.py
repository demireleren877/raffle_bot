import random
import smtplib
from email.message import EmailMessage


def login(server):
    server.login("demireleren1903@gmail.com", "usfdopgeawkmmlex")

def sendResult(to,text):
    msg = EmailMessage()
    msg["Subject"] = "Your Raffle Result 🎄🎁🎉"
    msg["From"] = "demireleren1903@gmail.com"
    msg["To"] = to
    msg.set_content(text)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        login(server)
        server.send_message(msg)

def shuffle_users(participants):
    users = participants.copy()
    random.shuffle(users)
    return users

    

def raffle(participants):    
    users = shuffle_users(participants)
    for i in range(len(users)):
        if i < len(users)-1:
            print(f"{users[i]['email']} gives to {users[i+1]['email']}")
            sendResult(users[i]['email'],f"You are giving gift to {users[i+1]['email']}")
        else:
            print(f"{users[i]['email']} gives to {users[0]['email']}")
            sendResult(users[i]['email'],f"You are giving gift to {users[0]['email']}")
    
