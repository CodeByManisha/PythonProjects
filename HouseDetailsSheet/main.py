from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
           "accept-language" : "en-US,en;q=0.9"}

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url, headers= headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")

links = []

for div in soup.find_all(name="div", class_="StyledPropertyCardDataWrapper"):
    a_tags = div.find_all("a")
    for a in a_tags:
        links.append(a.get("href"))

# print(links)

all_prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.getText().replace("/mo", "").split("+")[0] for price in all_prices]
# print(prices)

all_addresses = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
addresses = [add.getText().strip() for add in all_addresses]
# print(addresses)

# Part 2 - Fill in the Google Form using Selenium

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):
    # TODO: Add fill in the link to your own Google From
    driver.get("https://docs.google.com/forms/d/1iROVmwgoduTK6dGPKoRzVUhfkZpm4rH4qYTsjY_mcpk/edit")
    time.sleep(2)

    address = driver.find_element(by= By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")

    price = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

    link = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

    submit = driver.find_element(by=By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit.click()
