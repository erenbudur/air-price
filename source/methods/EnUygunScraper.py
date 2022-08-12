import email
import ssl
from click import password_option
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

context = ssl.create_default_context()

air_price_email = os.getenv('AIRPRICE_EMAIL')
my_email = os.getenv('MY_EMAIL')
password = os.getenv('AIRPRICE_PASSWORD')

body =  """
This is a test email
"""

email = EmailMessage()
email['From'] = air_price_email
email['To'] = my_email
email['subject'] = 'Test subject'
email.set_content(body)


with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
    server.login(air_price_email,password)
    server.sendmail(air_price_email,my_email,email.as_string())

