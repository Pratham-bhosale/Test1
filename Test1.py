import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

serv_obj = Service()
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(3)
driver.get("https://practicetestautomation.com/practice-test-login/")
username ="student"
password = "Password123"
name = "prathmesh"
last= "bhosale"
mail = "prathmesh@gmail.com"
Message= "Happy Diwali"
driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"submit").click()
time.sleep(2)
driver.find_element(By.XPATH,"//li[@id='menu-item-43']").click()
print(driver.find_element(By.CSS_SELECTOR,"h1").text)
driver.find_element(By.XPATH,"//li[@id='menu-item-18']").click()
driver.find_element(By.ID,"wpforms-161-field_0").send_keys(name)
driver.find_element(By.ID,"wpforms-161-field_0-last").send_keys(last)
driver.find_element(By.ID,"wpforms-161-field_1").send_keys(mail)
driver.find_element(By.ID,"wpforms-161-field_2").send_keys(Message)
time.sleep(2)
#driver.switch_to.frame("a-dbac7vvsud9j")
#driver.find_element(By.XPATH,"//iframe[@title='reCAPTCHA']")
#driver.switch_to.default_content()
  #driver.find_element(By.ID,"recaptcha-anchor").click()
#driver.find_element(By.ID,"recaptcha-anchor").click()
driver.find_element(By.ID,"wpforms-submit-161").click()
