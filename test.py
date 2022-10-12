from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

PATH = r"C:\Users\hp\Downloads\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(options=options , executable_path=PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)
driver.close()