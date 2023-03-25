from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time

import csv



#자동화된 크롬 창 실행

chrome_driver = ChromeDriverManager().install()

service = Service(chrome_driver)

driver = webdriver.Chrome(service=service)



#파파고 웹 페이지 접속

papago_url = 'https://papago.naver.com'

driver.get(papago_url)



time.sleep(3)



f = open('./my_papago.csv', 'r', encoding="utf-8-sig")



rdr = csv.reader(f)



next(rdr)



driver.find_element(By.CSS_SELECTOR, "button.btn_switch___x4Tcl").click()



for row in rdr:

    korean = row[1]

    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").send_keys(korean)

    driver.find_element(By.CSS_SELECTOR, "button#btnTranslate").click()



    time.sleep(1)



    output = driver.find_element(By.CSS_SELECTOR, "div#txtTarget")



    print(korean, ":", output.text)



    driver.find_element(By.CSS_SELECTOR, "textarea#txtSource").clear()



driver.close()

f.close()
