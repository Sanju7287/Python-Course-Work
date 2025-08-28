import emaillogic
rec_mail=input("Enter the email: ")
subject=input("Enter the subject: ")
body=input("Enter the body: ")
emaillogic.send_email(rec_mail,subject,body)