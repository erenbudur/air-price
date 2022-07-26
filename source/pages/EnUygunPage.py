
from bs4 import Tag
import click
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import locators


"""
Dates must be in the format of dd.mm.yyyy
"""
def searchEnUygun(departureDate,returnDate,numPeople,tripType):
           
    start_url = "https://www.enuygun.com/ucak-bileti/istanbul-boston-logan-intl-havalimani-ista-bos/?gidis="


    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver,10)
        #international
        driver.get(start_url + departureDate+ "&donus=" + returnDate + "&yetiskin=" + numPeople + "&sinif=ekonomi&save=1&geotrip=international&1trip=" + tripType)
        time.sleep(15)
        offerlist = driver.find_elements(By.XPATH,locators.FLIGHT_LIST)

        for trips in offerlist:
            trips.get


#searchEnUygun("26.08.2022","21.12.2022","1","international")