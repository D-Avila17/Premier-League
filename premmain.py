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

        home_team = driver.find_element(
            By.XPATH, '//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]').text
        away_team = driver.find_element(
            By.XPATH, '//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]').text
        # returns text 2-0
        scores = driver.find_element(
            By.XPATH, '//*[@id="mainContent"]/div/section/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div').text
        # assigns home and away team scores
        home_score = scores.split('-')[0]
        away_score = scores.split('-')[1]

        elem = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='tablist']//li[@data-tab-index='2']")))
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
        continue
    # dictionaries for each team 
    home_stats = {}
    away_stats = {}

    home_series = stats[home_team]
    away_series = stats[away_team]
    stats_series = stats['Unamed: 1']
    # data stored in rows
    for row in zip(home_series, stats_series, away_series):
        stat = row[1].replace('', '_').lower()
        home_stats[stat] = row[0]
        away_stats[stat] = row[2]
    # list containing all expected stats
    stats_check = ['possession_%', 'shots_on_target', 'shots', 'touches', 'passes', 
                'tackles', 'clearances', 'corners', 'offsides', 'yellow_cards', 
                'red_cards', 'fouls_conceded']
    # if any values in the list are not a key stat then stat is added to both dictionaries as zero
    for stat in stats_check:
        if stat not in home_stats.keys():
            home_stats[stat] = 0
            away_stats[stat] = 0

    match = [date, home_team, away_team, home_score, away_score, home_stats['possession_%'], away_stats['possession_%'],
            home_stats['shots_on_target'], away_stats['shots_on_target'], home_stats['shots'], away_stats['shots'],
            home_stats['touches'], away_stats['touches'], home_stats['passes'], away_stats['passes'],
            home_stats['tackles'], away_stats['tackles'], home_stats['clearances'], away_stats['clearances'],
            home_stats['corners'], away_stats['corners'], home_stats['offsides'], away_stats['offsides'],
            home_stats['yellow_cards'], away_stats['yellow_cards'], home_stats['red_cards'], away_stats['red_cards'],
            home_stats['fouls_conceded'], away_stats['fouls_conceded']]

    season.append(match)