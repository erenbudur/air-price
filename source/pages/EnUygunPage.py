
from lib2to3.pgen2 import driver
from locale import currency
from bs4 import Tag
import click
from numpy import double
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import locators

class Offer:
    def __init__(self,driver :webdriver.Chrome,offer) -> None:
        flights = offer.find_elements(By.CLASS_NAME,locators.FLIGHT)
        self.departure = Flight(driver,flights[0])
        self.arrival = Flight(driver,flights[1])
        self.price = float(offer.find_element(By.CLASS_NAME,locators.PRICE).text)
        self.currency = offer.find_element(By.CLASS_NAME,locators.CURRENCY).text

    def __str__(self) -> str:
        airlinesDepStr = ','.join(self.departure.airlines) 
        airlinesArrivalStr = ','.join(self.arrival.airlines) 
        var ="""
        Departure:
            Airlines:  {airDep}
            Time: {timeDep}
            Duration: {durDep}
        Return:
            Airlines:  {airArr}
            Time: {timeArr}
            Duration: {durArr}
        Price: {price} {currency}
        """.format(airDep=airlinesDepStr,airArr=airlinesArrivalStr,timeDep=self.departure.departureTime,timeArr=self.arrival.departureTime, durDep = self.departure.duration,durArr = self.arrival.duration, price = self.price, currency=self.currency)
        return var 

class Flight:
    def __init__(self,driver:webdriver.Chrome,flight) -> None:
        
        self.element = flight
        self.airlines = []
        companies = flight.find_elements(By.CLASS_NAME,locators.SUMMARY_AIRLINE)
        for company in companies:
            self.airlines.append(company.text)
        
        self.departureTime = flight.find_element(By.CLASS_NAME,locators.SUMMARY_TIME).text
        self.duration = flight.find_element(By.CLASS_NAME,locators.SUMMARY_DURATION).text
"""
Dates must be in the format of dd.mm.yyyy
"""
def searchEnUygun(departureDate,returnDate,numPeople,tripType):
           
    start_url = "https://www.enuygun.com/ucak-bileti/istanbul-boston-logan-intl-havalimani-ista-bos/?gidis="
    options = Options()
    options.headless = True

    with webdriver.Chrome(options=options) as driver:
        wait = WebDriverWait(driver,10)
        #international
        driver.get(start_url + departureDate+ "&donus=" + returnDate + "&yetiskin=" + numPeople + "&sinif=ekonomi&save=1&geotrip=international&1trip=" + tripType)
        driver.maximize_window()
        time.sleep(15)
        driver.find_element(By.XPATH,locators.TWO_TRANSFER).click()
        time.sleep(5)
        rawofferlist = driver.find_elements(By.XPATH,locators.OFFER_LIST)
        
    
        
        offerlist=[]

        for offers in rawofferlist:
            
            offer = Offer(driver,offers)
            offerlist.append(offer)
        
        return offerlist    

print('Done')