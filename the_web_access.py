import requests
'''
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

driver.get("https://www.skyscanner.net/")

Home = "LHR"
From = driver.find_element_by_xpath('//*[@id="fsc-origin-search"]')
From.send_keys(Home)

Destination = "Del"
To = driver.find_element_by_xpath('//*[@id="fsc-destination-search"]')
To.send_keys(Destination)

Direct = driver.find_element_by_xpath('//*[@id="flights-search-controls-root"]/div/div/form/div[2]/div[4]/label[1]')
Direct.click()
#driver.close()
'''


with open("the_file.txt", "r") as f:
    f_contents = f.read()
    print(f_contents)
