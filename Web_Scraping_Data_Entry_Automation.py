from bs4 import BeautifulSoup

import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
website = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

response = requests.get(url=website, headers=header)
response.raise_for_status()
content = response.text
soup = BeautifulSoup(content, "html.parser")

#Scraping all the links from the website
website = "https://www.zillow.com/"
link_list = []
list_of_links = soup.find_all(class_='property-card-link')
for links in list_of_links:
    link = links.get("href")
    updated_link = f"{website}{link}"
    link_list.append(updated_link)

# Scraping all the prices from the website
list_prices = []
list_of_prices = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 kJFQQX")
for prices in list_of_prices:
    price = prices.getText()
    price = price.replace("+ 1 bd", "")
    price = price.replace("$", "")
    price = price.replace(",","")
    price = price.replace("+/mo","")
    price = int(price)
    list_prices.append(price)

# Scraping all the addresses from the website
list_addresses = []
list_of_addresses = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-69-2__sc-yipmu-0 dZxoFm property-card-link")
for address in list_of_addresses:
    address = address.getText()
    list_addresses.append(address)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#TODO: convert it to internal variable with os
CHROME_DRIVER_PATH = "C:/Users/Leon/Desktop/pycharm_files/chromedriver.exe"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
index = 0
for i in range(len(list_addresses)-1):
    driver.get('your_google_form_link')
    time.sleep(3)

    address = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address.send_keys(list_addresses[index])

    price = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price.send_keys(list_prices[index])

    link = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link.send_keys(link_list[index])
    index+=1

    time.sleep(3)

    button = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")
    button.send_keys(Keys.ENTER)

    time.sleep(3)