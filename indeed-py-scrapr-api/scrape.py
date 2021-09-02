print("===DEBUT===")
from sys import platform
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from mongoengine import connect,Document, ListField, StringField, URLField
import flask
from flask import request, jsonify
from flask_cors import CORS

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config["ENV"] = "development"

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/jobs', methods=['GET'])
def getJobs():
    jobs = []
    if 'search' in request.args:
        link = "https://fr.indeed.com/Emplois-" + request.args['search']
        print(link)
        driver.get(link)
    else:
        driver.get("https://fr.indeed.com/emplois?q=developpeur+vue&l=")
    
    jobCards = driver.find_elements_by_css_selector(".result")

    for job in jobCards:

        jobTitle = "Not found"
        salary = "Undisclosed"
        summary = "Not found"
        try:
            jobTitle = driver.find_element_by_css_selector("#" + job.get_attribute("id") + " .jobTitle")
            jobTitle = jobTitle.text
        except NoSuchElementException:
            pass
        try:
            salary = driver.find_element_by_css_selector("#" + job.get_attribute("id") + " .salary-snippet")
            salary = salary.text
        except NoSuchElementException:
            pass

        try:
            summary = driver.find_element_by_css_selector("#" + job.get_attribute("id") + " .job-snippet")
            summary = summary.text
        except NoSuchElementException:
            pass
        

        json_job = {
            'title': jobTitle,
            'summary': summary,
            'salary': salary
        }

        jobs.append(json_job)
  
    return jsonify(jobs)

app.run(debug=True,host='0.0.0.0', port=9007)

driver.close()
print("===FIN===")
