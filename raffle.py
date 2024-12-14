import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import io
import random
import smtplib
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont


def img_crt(giver,receiver):
    image_path = "santa.jpg"  
    image = Image.open(image_path)
    
    font_path = "comic.ttf" 
    message_lines = [
            f"Merhaba {giver},",
            f"Bu yıl hediye alacağın kişi {receiver} !!!",
            "Mutlu Yıllar :)"
        ]
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=80)  
    line_spacing = 20 
    x = image.width / 2
    y = image.height /2 + 60
    for line in message_lines:
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        draw.text((x - text_width / 2, y), line, fill="black", font=font, align="center")
        y += draw.textbbox((0, 0), line, font=font)[3] + line_spacing
        
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0) 
    html_body = f"""
        <html>
          <body>
            <img src="cid:santa_image" alt="Santa Image"/>
          </body>
        </html>
        """
    
    image_part = MIMEImage(img_byte_arr.read(), name="santa_with_message.jpg")
    image_part.add_header('Content-ID', '<santa_image>') 


def login(server):
    server.login("demireleren1903@gmail.com", "usfdopgeawkmmlex")

def sendResult(to,text,giver,receiver):
    image_path = "santa.jpg"  
    image = Image.open(image_path)
    
    font_path = "comic.ttf" 
    message_lines = [
            f"Merhaba {giver},",
            f"Bu yıl hediye alacağın kişi {receiver} !!!",
            "Mutlu Yıllar :)"
        ]
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, size=80)  
    line_spacing = 20 
    x = image.width / 2
    y = image.height /2 + 60
    for line in message_lines:
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        draw.text((x - text_width / 2, y), line, fill="black", font=font, align="center")
        y += draw.textbbox((0, 0), line, font=font)[3] + line_spacing
        
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0) 
    html_body = f"""
    <html>
      <head>
        <style>
          /* Temel stil ayarları */
          body {{
            font-family: Arial, sans-serif;
            font-size: 16px;
          }}
          .email-content {{
            text-align: center;
          }}
          .email-text {{
            font-size: 18px;
            line-height: 1.5;
          }}
          img {{
            max-width: 100%;  /* Resmi ekran boyutuna göre küçültür */
            height: auto;     /* Yükseklik oranını korur */
          }}
    
          /* PC için özel stil */
          @media (min-width: 768px) {{
            .email-text {{
              font-size: 14px; /* PC'de metin boyutunu küçült */
            }}
            img {{
              max-width: 60%;  /* PC'de resmi daha küçük yap */
            }}
          }}
    
          /* Mobil için özel stil */
          @media (max-width: 767px) {{
            .email-text {{
              font-size: 18px;  /* Mobilde metin boyutunu büyük tut */
            }}
            img {{
              max-width: 100%;  /* Mobilde resmi tam genişlikte göster */
            }}
          }}
        </style>
      </head>
      <body>
        <div class="email-content">
          <img src="cid:santa_image" alt="Santa Image"/>
        </div>
      </body>
    </html>
    """
    image_part = MIMEImage(img_byte_arr.read(), name="santa_with_message.jpg")
    image_part.add_header('Content-ID', '<santa_image>') 

    msg = EmailMessage()
    msg = MIMEMultipart()
    msg["Subject"] = "Your Raffle Result 🎄🎁🎉"
    msg["From"] = "demireleren1903@gmail.com"
    msg["To"] = to
    msg.attach(MIMEText(html_body, "html")) # Burada CID ile ilişkilendiriyoruz
    msg.attach(image_part)
    #msg.set_content(text)
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
            sendResult(users[i]['email'],f"You are giving gift to {users[i+1]['email']}",giver=users[i]['username'],receiver=users[i+1]['username'])
        else:
            print(f"{users[i]['email']} gives to {users[0]['email']}")
            sendResult(users[i]['email'],f"You are giving gift to {users[0]['email']}",giver=users[i]['username'],receiver=users[0]['username'])
    
