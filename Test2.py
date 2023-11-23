from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://the-internet.herokuapp.com/login")
username= "tomsmith"
passs= "SuperSecretPassword"
driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(passs)
driver.find_element(By.XPATH,"//i[@class='fa fa-2x fa-sign-in']").click()


