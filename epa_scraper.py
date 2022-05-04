from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import csv

# Path to csv file that will store data 
file_path = '/Users/williamlanghorne/Desktop/web_scrapers/outputs/epa.csv'

# Add header for the first row of data
headers = ['Facility name', 'Chemical', 'Percentage spike', 'Spike duration']

# Write headers 
with open(file_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    f.close()

# Initiate driver
URL = 'https://enviro.epa.gov/triexplorer/release_fac?P_VIEW=STFA&fld=&trilib=TRIQ1&TAB_RPT=1&sort=_VIEW_&Fedcode=&FLD=RELLBY&FLD=TSFDSP&sort_fmt=1&industry=ALL&STATE=05&COUNTY=All+counties&chemical=All+chemicals&YEAR=2020&TopN=ALL' 
s = Service('/Users/williamlanghorne/Desktop/web_scrapers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get(URL)

# Get emission table, rows   
table = driver.find_elements(By.CSS_SELECTOR, 'table')[3]
rows = table.find_elements(By.CSS_SELECTOR, 'tr')

# Iterate through rows 
for row in rows[3:]:
  # Get facility link
  link = row.find_elements(By.CSS_SELECTOR, 'td')[1]
  



