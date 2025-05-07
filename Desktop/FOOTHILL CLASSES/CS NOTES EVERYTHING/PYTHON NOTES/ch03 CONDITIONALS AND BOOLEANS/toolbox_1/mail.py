##
#  This program allows you to notify multiple students of their test scores
#  via e-mail. It illustrates how to send an e-mail message using tools in 
#  Python's standard library.
#

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Set email header information.
sender = "sally.smith@mycollege.edu"
username = "sallysmith"
password = input("Password: ")
host = "smtp.myserver.com"
port = 587

# Read the test score from the user.
recipient = input("Student email: ")
score = int(input("Score: "))
body = "Your score on the last exam is " + str(score) + "\n"
if score <= 50 :
   body = body + "To do better next time, why not visit the tutoring center?"
elif score >= 90 :
   body = body + "Fantastic job! Keep it up."

# Assemble the message.
msg = MIMEMultipart()
msg.add_header("From", sender)
msg.add_header("To", recipient)
msg.add_header("Subject", "Exam score")
msg.attach(MIMEText(body, "plain"))         

# Send the message.
server = smtplib.SMTP(host, port)
server.starttls()
server.login(username, password)
server.send_message(msg)
server.quit()

