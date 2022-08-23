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
from datetime import date
from enUygunPage import searchEnUygun


load_dotenv()

context = ssl.create_default_context()

air_price_email = os.getenv('AIRPRICE_EMAIL')
my_email = os.getenv('MY_EMAIL')
password = os.getenv('AIRPRICE_PASSWORD')
dateDep = "26.08.2022"
dateReturn = "21.12.2022"
offers = searchEnUygun(dateDep,dateReturn,"1","international")
body =  f"""
These are the best three flight tickets from Istanbul to Boston with a depature date of {dateDep} and a return date of {dateReturn}: \n
"""

for i in range(1,4):
    body += ("\n Offer " + str(i) + ': \n' + str(offers[i-1]))



today = date.today()
date = today.strftime("%d/%m/%Y")
email = EmailMessage()
email['From'] = air_price_email
email['To'] = my_email
email['subject'] = 'Flight tickets for the date of ' + str(date)
email.set_content(body)




with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
    server.login(air_price_email,password)
    server.sendmail(air_price_email,my_email,email.as_string())
    print('Mail sent!')

