from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
soup = BeautifulSoup(browser.page_source, "html.parser")
def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    starNames_data = []
    Distance = []
    Mass = []
    Radius = [] 
    starTable = soup.find('tbody')
    temp_list = []
    tableRows = starTable.find_all('tr')
    for i in tableRows:
        td = tableRows.find('td')
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
    for i in range(1,len(temp_list)):
        starNames_data.append(temp_list[i][1])
        Distance.append(temp_list[i][3])
        Mass.append(temp_list[i][5])
        Radius.append(temp_list[i][6])
    df2 = pd.DataFrame(list(zip(starNames_data,Distance,Mass,Radius)), columns = ['starNmaes_data','Distance','Mass','Radius'])
    print(df2)
scrape()