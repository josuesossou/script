import sys
from selenium import webdriver


browser = webdriver.Chrome()

browser.get('https://github.com/login')

inputElement = browser.find_element_by_id("login_field")
inputElement.send_keys('josuesossou8@gmail.com')

inputElement = browser.find_element_by_id("password")
inputElement.send_keys('Iamn0t@robot')

buttonElement = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
buttonElement.click()

browser.get('https://github.com/new')

inputElement = browser.find_element_by_id('repository_name')
inputElement.send_keys(sys.argv[1])

inputElement = browser.find_element_by_id('repository_description')
inputElement.send_keys(sys.argv[2])

submitElement = browser.find_element_by_css_selector('#new_repository > div.js-with-permission-fields > button')
submitElement.submit()

browser.close()
browser.quit()





