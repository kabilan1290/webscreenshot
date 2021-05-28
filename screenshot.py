from selenium import webdriver
import time
import datetime

DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
file1 = open('gupie.txt', 'r') //file containing URL
Lines = file1.readlines()
date_stamp = str(datetime.datetime.now()).split('.')[0]
date_stamp = date_stamp.replace(" ", "_").replace(":", "_").replace("-", "_")

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    a=line.strip()
    driver.get(a)
    time.sleep(6)
    b = str(a)
    a = a.replace("site.com", "_")
    screenshot = driver.save_screenshot(date_stamp+a+"mytest.png")
    time.sleep(1)
driver.quit()
