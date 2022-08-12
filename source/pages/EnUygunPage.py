
from lib2to3.pgen2 import driver
from bs4 import Tag
import click
from numpy import double
from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import locators

class Offer:
    def __init__(self,driver :webdriver.Chrome,offer) -> None:
        flights = offer.find_elements(By.CLASS_NAME,locators.FLIGHT)
        self.departure = Flight(driver,flights[0])
        self.arrival = Flight(driver,flights[1])
        self.price = float(offer.find_element(By.CLASS_NAME,locators.PRICE).text)
        self.currency = offer.find_element(By.CLASS_NAME,locators.CURRENCY).text

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


    with webdriver.Chrome() as driver:
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
        
        print('')


searchEnUygun("26.08.2022","21.12.2022","1","international")

