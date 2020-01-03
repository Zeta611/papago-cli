#!/usr/bin/env python
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True
browser = Chrome(options=options)
browser.get("https://papago.naver.com")

timeout = 10
try:
    txt_source = WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((By.ID, "txtSource"))
    )
    txt_target = WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located((By.ID, "txtTarget"))
    )

    to_translate = input("번역할 내용을 입력하세요: ")
    txt_source.send_keys(to_translate)
    while txt_target.text == "" or txt_target.text[-3:] == "...":
        continue
    print("번역된 결과입니다:", txt_target.text)
finally:
    browser.quit()
