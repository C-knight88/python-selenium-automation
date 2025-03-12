from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# BY ID
Amazon logo, driver. find_element(By ID, 'nav-logo-sprites')
Email field, driver. find_element(By ID, 'ap_email')
Continue button, driver. find_element(By ID, 'continue')
Conditions of use link, driver.find_element(By ID, 'a-page')
Need help link, driver. find_element(By ID, "authportal-main-section')
Forgot Password link, driver. find_element(By ID, 'auth-fpp-link-bottom')
Other issues with Sign-In link, driver. find_element(By ID, 'ap-other-signin-issues-link')
Create your amazon account button, driver. find_element(By ID, 'createAccountSubmit')


