from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("Annaram")

last_Name = driver.find_element(By.NAME,"lName")
last_Name.send_keys("Manisha")

email = driver.find_element(By.NAME,"email")
email.send_keys("mittubytes@gmail.com")

# <button class="btn btn-lg btn-primary btn-block" type="submit" fdprocessedid="14e4js">Sign Up</button>
sign_up = driver.find_element(By.CSS_SELECTOR,"form button")
sign_up.click()