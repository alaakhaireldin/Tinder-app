import os
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

import time


username = os.environ.get("FB_EMAIL")
password = os.environ.get("PASSWORD")
tinder_link = 'https://tinder.com/app/recs'
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(tinder_link)

time.sleep(3)

log_in = driver.find_element_by_link_text('Log in')
log_in.click()
time.sleep(3)

facebook_log_in = driver.find_element_by_xpath('//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_log_in.click()
time.sleep(3)
base_window = driver.window_handles[0]
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
email_input = driver.find_element_by_xpath('//*[@id="email"]')
email_input.send_keys(username)
password_input = driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(5)
ACCEPT_cookies = driver.find_element_by_xpath('//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button')
ACCEPT_cookies.click()
time.sleep(1)
allow_location = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(1)
NOT_INTERESTED = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
NOT_INTERESTED.click()
time.sleep(9)

dislike = driver.find_element_by_css_selector('.Mx\(a\):nth-child(2) .Scale\(\.5\)')
while True:
    time.sleep(2)
    if dislike.is_displayed():
        try:
            dislike.click()
        except ElementClickInterceptedException:
            not_interested = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click()
    else:
        print('a bug')
        continue

