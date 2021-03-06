
from selenium import webdriver

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    user_input = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    
    
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path= './chromedriver.exe', options=options)
    

    driver.get("https://www.skyscanner.net/")    
    
    cookie = driver.find_element_by_xpath('//*[@id="cookie-banner-root"]/div[1]/div/div[2]/button[1]')
    cookie.click()
    
    
    '''
    theTicket = user_input[1]
    Ticket = driver.find_element_by_xpath('//*[@id="flights-search-controls-root"]/div/div/form/div[1]/div')
    Ticket.click()
    '''
    
    Destination = user_input[2]
    To = driver.find_element_by_xpath('//*[@id="fsc-destination-search"]')
    To.send_keys(Destination)
    
    Home = user_input[3]
    From = driver.find_element_by_xpath('//*[@id="fsc-origin-search"]')
    From.send_keys(Home)
    '''
    DepartDate = user_input[4]
    Depart = driver.find_element_by_xpath('//*[@id="depart-fsc-datepicker-button"]/span')
    Depart.send_keys(DepartDate)
    
    ReturnDate = user_input[5]
    Return = driver.find_element_by_xpath('//*[@id="fsc-destination-search"]')
    Return.send_keys(ReturnDate)
    
    theClass = user_input[6]
    Class = driver.find_element_by_xpath('//*[@id="search-controls-cabin-class-dropdown"]')
    Class.click()
    
        
    theDirect = user_input[8]
    Direct = driver.find_element_by_xpath('//*[@id="flights-search-controls-root"]/div/div/form/div[2]/div[4]/label[1]')
    Direct.click()
    #driver.close()
    '''
readFile('flightData.txt')