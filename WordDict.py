# 나만의 번역 사전 만들기
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time



chrome_driver = ChromeDriverManager().install()

service = Service(chrome_driver)

driver = webdriver.Chrome(service=service)



URL = "https://papago.naver.com/"

driver.get(URL)

time.sleep(3)



dict = {}



while 1:

  question = input("번역 할 영단어를 입력 (0을 입력하면 종료됩니다.) : ")

  

  if question == '0':

    break



  form = driver.find_element(By.CSS_SELECTOR, "textarea#txtSource")

  form.send_keys(question)



  button = driver.find_element(By.CSS_SELECTOR, "button#btnTranslate")

  button.click()

  time.sleep(2)



  result = driver.find_element(By.CSS_SELECTOR, "div#txtTarget")

  dict[question] = result.text



  form.clear()



print(dict)



driver.close()

