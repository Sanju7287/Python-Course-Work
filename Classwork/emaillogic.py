import smtplib #Simple Mail Transfer Protocol for sending emails
import os #For file path and file existence checks
import csv #To read email addresses from a CSV file
from email.mime.multipart import MIMEMultipart
#For creating mutipart email messages
from email.mime.text import MIMEText
#For adding plain text to email body
#https://myaccount.google.com/apppasswords
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587 #port used for TLS (encryption)
SENDER_EMAIL="chandrasanjaykumar01@gmail.com"
SENDER_PASSWORD="ocnh ybbt ovoj vled"
def send_email(to_email,subject,body):
    try:
        msg=MIMEMultipart()
        msg["From"]=SENDER_EMAIL
        msg["To"]=to_email
        msg["Subject"]=subject
        msg.attach(MIMEText(body,"Plain"))
        server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,to_email,msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}:{e}")
        
def send_bulk_emails(csv_file,subject,body):
    try:
        csv_path=os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error: CSV file'{csv_file}'not found.")
            return
        with open(csv_path,newline="",encoding="utf-8") as file:
            reader=csv.reader(file)
            next(reader,None)
            for row in reader:
                if row:
                    email=row[0]
                    send_email(email,subject,body)
    except Exception as e:
        print(f"Error reading CSV file: {e}")