import logging
import smtplib
import datetime
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import os
from . import config
# Setup logs
logging.basicConfig(filename='report.log', level=logging.DEBUG)

SENDER = 'husmani@fluids.ai'
SENDERNAME = 'forecastai.biz'

RECIPIENTS  = None

USERNAME_SMTP = config.email_user
PASSWORD_SMTP = config.email_pass


HOST = config.email_host
PORT = config.email_port

# The subject line of the email.
SUBJECT = 'forecastai.biz Notification'

def send_email(body, recipient) :
  BODY_HTML = body
  # Create message container - the correct MIME type is multipart/alternative.
  msg = MIMEMultipart('alternative')
  msg['Subject'] = SUBJECT
  msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
  # Comment or delete the next line if you are not using a configuration set
  # msg.add_header('X-SES-CONFIGURATION-SET',CONFIGURATION_SET)

  # Record the MIME types of both parts - text/plain and text/html.
  part1 = MIMEText(BODY_HTML, 'plain')
  part2 = MIMEText(BODY_HTML, 'html')

  # Attach parts into message container.
  # According to RFC 2046, the last part of a multipart message, in this case
  # the HTML message, is best and preferred.
  msg.attach(part1)
  msg.attach(part2)

  # Try to send the messages to the recipients
  # RECIPIENTS must be comma separated
  msg['To'] = recipient
  try:
    server = smtplib.SMTP(HOST, PORT)
    server.ehlo()
    server.starttls()
    #stmplib docs recommend calling ehlo() before & after starttls()
    server.ehlo()
    server.login(USERNAME_SMTP, PASSWORD_SMTP)
    server.sendmail(SENDER, RECIPIENTS, msg.as_string())
    server.close()
  # Display an error message if something goes wrong.
  except Exception as e:
    print ("Error: ", e)
  else:
    print (f"Email sent to {RECIPIENTS}")
  
  return BODY_HTML
