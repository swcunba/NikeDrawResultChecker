# windows cmd에 C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os, sys

#/html/body/footer/div/div[1]/div/div/p[4]/a: 로그아웃 xpath.
#/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[1]/div[1]/span[2]: 당첨여부 xpath.
#/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]: 품명 xpath
## 크롬 웹 드라이버
os.system('C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path = "C:/Users/user/Desktop/유승우/ChatBot/chromedriver", options=options)

# 웹 드라이버 로딩 대기()
driver.implicitly_wait(3)

# html 문서 가져올 url
driver.delete_all_cookies()
driver.get("https://www.nike.com/kr/ko_kr/login?successUrl=/account/theDrawList")

def login():
    #계정, 비밀번호, 로그인 버튼 클릭.
    email_input = driver.find_element_by_xpath("//input[@name='j_username']")
    email_input.clear()
    email_input.send_keys("swcunba@nate.com")
    time.sleep(1)

    password_input = driver.find_element_by_xpath("//input[@name='j_password']")
    password_input.clear()
    password_input.send_keys("dbtmddn1!")
    time.sleep(1)

    login_xpath = "/html/body/section/section/div[2]/div/div[2]/div/div[2]/div/button"
    driver.find_element_by_xpath(login_xpath).click()
    time.sleep(1)

def scrap():
    outer_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]"
    product_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/span[1]"
    product = driver.find_element_by_xpath(outer_xpath).find_elements_by_xpath(product_xpath)
    for p in product:
        print(p.text)

    result_xpath = "/html/body/section/section/article[2]/div/div[2]/div/div[2]/div[1]/div[1]/span[2]"
    result = driver.find_element_by_xpath(outer_xpath).find_elements_by_xpath(result_xpath)
    for r in result:
        print(r.text)

def logout():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")    
    logout_xpath = "/html/body/footer/div/div[1]/div/div/p[4]/a"
    driver.find_element_by_xpath(logout_xpath).click()

login()
scrap()
logout()
