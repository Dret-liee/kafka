from kafka import KafkaConsumer
import json
import ssl
import smtplib
from email.message import EmailMessage
import mysql.connector




consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Dretliee13865557@",
    database="test"
)
cursor = db.cursor()


for msg in consumer:
    payload = json.loads(msg.value)
    fname = payload.get('First name')
    city = payload.get('City')
    country = payload.get('Country')

    if payload.get('Country') == 'Canada':

        # email_sender = 'dretliee@gmail.com'
        # email_receiver = 'dretliee@gmail.com'
        # password = 'lrxp onsb slqu ygrh'
        
        # subject = 'Kafka found something'
        # body = f'{payload}'
        
        # em = EmailMessage()
        # em['From'] = email_sender
        # em['To'] = email_receiver
        # em['Subject'] = subject
        # em.set_content(body)
        
        # context = ssl.create_default_context()
        
        # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        #     smtp.login(email_sender, password)
        #     smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        
        cursor.execute("INSERT INTO messages (fname, city, country) VALUES (%s, %s, %s)", (fname, city, country))
        db.commit()
        print('message sent')

    else:
        continue


