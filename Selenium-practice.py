from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com")
#driver.back()
#driver.forward()
#driver.refresh()

#Finding Elements
content_element = driver.find_element(By.ID,"content")
#print(element)
element = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[30]/a')
#print(element)


print("Content Link text:", content_element.text)
print("Link text:", element.text)

#Wait  
wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.ID,"content")))

#interactions
element.click()
#element.send_keys("Vijayanand")
#element.clear()
wait = WebDriverWait(driver,1000)

#Screenshots
driver.save_screenshot("screenshot-Selenium.png")