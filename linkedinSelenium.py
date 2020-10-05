# ------------- SETTINGS ---------------------------
from selenium import webdriver
import time

driver_path = "/home/x/Desktop/FY/SeleniumInstagram/chromedriver"
browser = webdriver.Chrome(driver_path)
# --------------------------------------------------

browser.get("https://www.linkedin.com/") # LinkedIn'i AÇ
time.sleep(3)

# -------- LOGIN İŞLEMİ ----------------------------
username = browser.find_element_by_name("session_key")
password = browser.find_element_by_name("session_password")

username.send_keys('frknyldz8489@gmail.com')
password.send_keys('XXXXXXXXXX')

loginButton = browser.find_element_by_class_name('sign-in-form__submit-button')
time.sleep(4)
loginButton.click()
# --------------------------------------------------


# -------- PROFILE GEÇİŞ İŞLEMİ ----------------------------
time.sleep(7)
profileButton = browser.find_element_by_class_name('profile-rail-card__actor-link')
profileButton.click()
time.sleep(7)
# --------------------------------------------------


browser.quit() 