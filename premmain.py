# File created by: Diego Avila
# Sources: https://automatetheboringstuff.com/2e/chapter12/
# Sources: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/#
# Sources: https://www.kdnuggets.com/2020/11/build-football-dataset-web-scraping.html

'''
Goals: create a program that helps me predict who will win the Premier League
and get relegated based on existing data
'''
# libraries used
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import pandas as pd

errors = []
season = []

# range of premier league games 22/23 season from August 5 till May 21
for id in range(74911, 75275):
    # link to any of games
    my_url = f"https://www.premierleague.com/match/{id}"
    option = Options()
    # broswer will not open and go to the website to collect data
    option.headless = True
    driver = webdriver.Chrome(options=option)
    # loads url into webpage
    driver.get(my_url)

date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
    By.XPATH, '//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]'))).text
date = datetime.strptime(date, "%a %d %b %Y").strftime("%m/%d/%Y")

home_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
away_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text