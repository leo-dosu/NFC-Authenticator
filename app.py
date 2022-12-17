from ast import dump
from itertools import count
from pickle import GET
import re
import requests
import resource
from unicodedata import name
from urllib import  response
from webbrowser import get
from wsgiref import validate

#framework packages
from flask import Flask, request, json, jsonify
from crypt import methods

#custom packages
from crawler import crawl
from crawler import const
from views import page_views

#temporal
from selenium.webdriver.common.by import By
import pandas as pd
from lxml import etree
#bs4
from bs4 import BeautifulSoup

#app instance with configuration files
app = Flask(__name__)


@app.route('/validate', methods = ['GET', 'POST'])
def job():
    driver = crawl.loadDriver()
    student_data = []
    driver.get(const.url)
    network_check = crawl.is_cnx_active
    if network_check == False:
        return "SERVER CONNECTION FAILED"
    else:
        crawl.loadDriverDelay()
        check_page_loaded = crawl.check_status(driver)
        crawl.login(driver, const.matric, const.password)
        crawl.scroll_click_element(driver, const.bio_data_element)
        crawl.loadWebPageDelay()

        data = requests.get(driver.current_url)
        student_data = driver.find_elements(By.XPATH, "//table[@class='table table-responsive']//tbody//tr[1]")
        (student_data)
        name = "Dosu Leo"
        matricNumber = "F/HD/20/3210115"
        # soup = BeautifulSoup(data.text, 'html.parser')

        # tabs = soup.find("table")
        # return dict(tabs)
        # Collecting Ddata
        # for row in tabs.tbody.find_all('tr'):    
        #     columns = row.find_all('td')
        #     print(columns)
        response = jsonify(
        {'message' : 'web driver loaded'}, 
        { 'message':  check_page_loaded },
        {'Student Data' : 'th'})
        response.status_code = 200
        return response

def checkData():
    pass

# route defination to the dashboard
@app.route('/',  methods=['GET'])
def checkAPI():
    response = jsonify('boom play !')
    response.status_code = 200
    return response



# get matric number and last-name/password input from api 
# @app.route('/student', methods = ['GET', 'POST'])
# def get_student():
#     if request.method == 'GET':
#         response = jsonify({'Data' : menu })
#         response.status_code = 200
#         return response




# route to render the student Data
@app.route('/s',  methods=[GET])
def studentData():
    pass

#run app
if __name__ == "__main__":
    app.run(debug=True)

