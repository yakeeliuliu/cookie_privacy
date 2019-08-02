# drive resources: http://chromedriver.storage.googleapis.com/index.html
# unzip to /usr/bin
# to run google in kali: google-chrome --no-sandbox

from selenium import webdriver
 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.google.com")

print(driver.get_cookies()) 
 
