# File created by: Diego Avila
# Sources: https://automatetheboringstuff.com/2e/chapter12/
# Sources: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/#
# Sources: https://www.kdnuggets.com/2020/11/build-football-dataset-web-scraping.html
# Sources: selenium_chromedriver_scrape.py
# Sources: https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
# Sources: selenium_chromdriver_scrape_to_excel.py
'''
Goals: webscrape data from the first game of the 22/23 Premier League
'''
# libraries used
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd
import os
from pathlib import Path
import xlwt
from xlwt import Workbook
# site to scrape data
URL = 'https://www.premierleague.com/match/74911'

chrome_driver = "Code\Projects\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get(URL)
sleep(5)

elem = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='tablist']//li[@data-tab-index='2']")))
elem.click()
sleep(5)

searchresults = driver.find_elements(By.XPATH,"//*[contains(@class,'mcStatsTab statsSection season-so-far wrapper col-12 active')]")
print(searchresults[0].text)

# datafound = []

# for i in searchresults:
#     if len(i.text) > 0:
#         datafound.append(i.text)
#     if len(datafound) > 45:
#         break