from lib2to3.pgen2 import driver
import re
import time
import random

#framework packages
from flask import Flask, request, json, jsonify
from crypt import methods
from pickle import GET
from urllib import  response

#custom packages
from crawler import const
from views import page_views

# define the method to login & fetch user data
import string

# network packages
import requests


#selenium packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from typing import Any, AnyStr


# test network connection
def is_cnx_active():
    try:
        requests.head("http://www.google.com/", timeout=4)
        return True
    except requests.ConnectionError:
        return False

#custom wait 
def loadWebPageDelay():
    time.sleep(random.randint(4,7))

def loadDriverDelay():
    time.sleep(random.randint(3,7))

#driver 
def loadDriver():
    option = webdriver.FirefoxOptions()
    # option.headless = True
    # option.add_argument('--no-sandbox')
    # option.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Firefox(options=option)
    return driver
    

#confirm page loaded if not reload
def check_status(driver): 
    try:
        ele = WebDriverWait(driver, 10).until #using explicit wait for 10 seconds
        (EC.presence_of_element_located((By.ID, 'login')) #checking for the element with 'h2'as its CSS
    )
        return "Page is loaded within 10 seconds."
    except:
        return "Timeout Exception: Page did not load within 10 seconds."


def scroll_click_element(driver, xpath):
    scroll_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, xpath)))
    driver.execute_script("arguments[0].click();", scroll_element)
    # driver.find_element(By.XPATH, xpath).click()
    time.sleep(0.4)

# login student in 
def login(driver: any, matric: string, password: Any, ):
    driver.find_element(By.NAME, "matric_number").send_keys(matric) 
    driver.find_element(By.NAME, "password").send_keys(password)
    driver. find_element(By.ID, 'login').click()
    loadWebPageDelay()

    # driver.get('https://portal.yabatech.edu.ng/portalplus/?pg=biodata')
    



# get student data
# def fetchData(driver):
#     data = []
#     data.append(driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/th').text)
#     return data


    
def get_name():
#    method fetch student's name
    pass

def get_image(): 
    # method fetches student's image
    pass
