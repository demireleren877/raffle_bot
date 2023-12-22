import random
import smtplib
from email.message import EmailMessage
import imaplib
import email.message
from email import policy


def login(server):
    server.login("demireleren1903@gmail.com", "ceuqchabyttkvwig")

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
    receivers = participants.copy()
    random.shuffle(receivers)
    givers = participants.copy()
    random.shuffle(givers)
    pairs = list(zip(givers, receivers))
    return pairs

    

def raffle(participants):
    arrayInequality = True
    pairs = shuffle_users(participants)
    for i in range(len(pairs)):
        if pairs[i][0] == pairs[i][1]:
            arrayInequality = False
    if arrayInequality :
        for receiver,giver in pairs:
            sendResult(giver['email'],f"You are giving gift to {receiver['username']}")
    else:
        raffle(participants)
 