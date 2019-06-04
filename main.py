#!/usr/bin/env python
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

options = Options()
options.headless = True
browser = Chrome(options=options)
browser.get("https://papago.naver.com")

timeout = 10
start = time.time()
while time.time() - start < timeout:
    try:
        txt_source = browser.find_element_by_id("txtSource")
        txt_target = browser.find_element_by_id("txtTarget")
        break
    except NoSuchElementException:
        continue
if "txt_source" not in locals() or "txt_target" not in locals():
    raise TimeoutException(f"Aborted due to a timeout ({timeout}s)")

to_translate = input("번역할 내용을 입력하세요: ")
txt_source.send_keys(to_translate)
while txt_target.text == "" or txt_target.text[-3:] == "...":
    continue
print("번역된 결과입니다:", txt_target.text)

browser.quit()

