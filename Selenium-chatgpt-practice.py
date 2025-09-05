import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver with waits
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# 1. Test Checkboxes
def test_checkboxes():
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))
    time.sleep(5)
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
        assert all(cb.is_selected() for cb in checkboxes), "Not all checkboxes were selected."

# Run all tests
try:
    test_checkboxes()
    print("✅ Checkboxes test passed.")
finally:
    driver.quit()