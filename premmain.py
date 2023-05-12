# File created by: Diego Avila
# Sources: https://automatetheboringstuff.com/2e/chapter12/
# Sources: https://www.geeksforgeeks.org/how-to-install-selenium-in-python/#
# Sources: https://www.kdnuggets.com/2020/11/build-football-dataset-web-scraping.html

'''
Goals: webscrape data from the beginning of the 22/23 Premier League season till May 14
'''
# libraries used
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
import pandas as pd

errors = []
season = []

# range of premier league games 22/23 season from August 5 till May 14
for id in range(74911, 75270):
    # link to any of games
    my_url = f"https://www.premierleague.com/match/{id}"
    option = Options()
    # broswer will not open and go to the website to collect data
    option.headless = True
    driver = webdriver.Chrome(options=option)
    # loads url into webpage
    driver.get(my_url)
# error handling
# will append the match id to the errors list and move to next match without crashing
try:
    
    # This is one of the parts of the page generated using JavaScript
    # WebDriverWait waits for the element to be rendered to avoid raising an error
    date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="mainContent"]/div/section/div[2]/section/div[1]/div/div[1]/div[1]'))).text
    date = datetime.strptime(date, '%a %d %b %Y').strftime('%m/%d/%Y')

    home_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
    away_team = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text
    # returns text 2-0
    scores = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div').text
    # assigns home and away team scores
    home_score = scores.split('-')[0]
    away_score = scores.split('-')[1]

    elem = WebDriverWait(driver, 20). until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='tablist']//li[@data-tab-index='2']")))
    elem.click()
    sleep(3)
    # read_html function returns a list with all tables on the page stored as dataframes
    dfs = pd.read_html(driver.page_source)
    stats = dfs[-1]

    driver.quit()
# error handling
except:
    driver.quit()
    errors.append(id)
