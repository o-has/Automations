from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('ENTER YOUR WEBSITE')
time.sleep(5) # Let the user actually see something!

#emailbox = driver.find_element("id", "BaseFormInput:email:4")
#emailbox.click()
#time.sleep(2)

#emailbox.send_keys('ENTER YOUR INFO')

#pwordbox = driver.find_element("id", "BaseFormInput:password:5")
##pwordbox.click()
#pwordbox.send_keys('ENTER YOUR INFO')

#submitbutton = driver.find_element(By.type, "submit")
#submitbutton.click()

#loginbutton = driver.find_element("id", "login-form")
#loginbutton.click()
#Firstname = driver.find_element("id", "BaseFormInput:first_name:1")
#Firstname.click()
#time.sleep(2)

#Firstname.send_keys('ENTER YOUR INFO')

#Lastname = driver.find_element("id", "BaseFormInput:last_name:2")
#Lastname.click()
#Lastname.send_keys('ENTER YOUR INFO')
#time.sleep(20)
#loginbutton = driver.find_element("id", "baseform-submit-button")
#loginbutton.click()
#time.sleep(200)
