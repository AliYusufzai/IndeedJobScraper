import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
#options = webdriver.ChromeOptions() 
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
webdriver_service = Service('C:\\Users\\hp\\Downloads\\chromedriver\\chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service)

def get_current_url(url, job_title, location):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.find_element('xpath','//*[@id="text-input-what"]').send_keys(job_title)
    time.sleep(3)
    driver.find_element('xpath','//*[@id="text-input-where"]').send_keys(location)
    time.sleep(3)
    driver.find_element('xpath','/html/body/div').click()
    time.sleep(3)
    try:
        driver.find_element('xpath','//*[@id="jobsearch"]/button').click()
    except:
        driver.find_element('xpath','//*[@id="whatWhereFormId"]/div[3]/button').click()
    current_url = driver.current_url
    return current_url

current_url = get_current_url('https://pk.indeed.com/', 'Python Developer', 'Karachi')
print(current_url)

def get_jobs(url):
    response = requests.get(url, headers=HEADERS)
    content = BeautifulSoup(response.content, 'lxml')
    job_lists = []
    for post in content.select('.job_seen_beacon'):
        try:
            data = {
                "job_title":post.select('.jobTitle')[0].get_text().strip(),
                "company":post.select('.companyName')[0].get_text().strip(),
                "rating":post.select('.ratingNumber')[0].get_text().strip(),
                "location":post.select('.companyLocation')[0].get_text().strip(),
                "date":post.select('.date')[0].get_text().strip(),
                "job_desc":post.select('.job-snippet')[0].get_text().strip()
            }
        except IndexError:
            continue
        job_lists.append(data)
    print(job_lists)
    dataframe = pd.DataFrame(job_lists)
    return dataframe
get_jobs(current_url)
df = get_jobs(current_url)
print(df)
