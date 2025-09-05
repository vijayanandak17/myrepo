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
    time.sleep(2)
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
    assert all(cb.is_selected() for cb in checkboxes), "Not all checkboxes were selected."

# 2. Test Dropdown
def test_dropdown():
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    time.sleep(2)
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option 2")
    selected_option = dropdown.first_selected_option.text
    assert selected_option == "Option 2", f"Dropdown selection failed, got {selected_option}"

# 3. Test Login (Form Authentication)
def test_login():
    driver.get("https://the-internet.herokuapp.com/login")

    # Invalid Login
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "Your username is invalid!" in error_msg

    # Valid Login
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    success_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash"))).text
    assert "You logged into a secure area!" in success_msg

# 4. Test JavaScript Alerts
def test_alerts():
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    alert_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Alert']")))
    time.sleep(2)
    alert_button.click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == "I am a JS Alert"
    alert.accept()
    result = wait.until(EC.visibility_of_element_located((By.ID, "result"))).text
    assert result == "You successfully clicked an alert", f"Unexpected result: {result}"

# 5. Test Dynamic Loading (Example 1)
def test_dynamic_loading():
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
    time.sleep(5)
    start_button.click()
    result = wait.until(EC.visibility_of_element_located((By.ID, "finish"))).text
    assert result == "Hello World!", f"Dynamic loading failed. Got: {result}"

# Run all tests
try:
    test_checkboxes()
    print("✅ Checkboxes test passed.")

    test_dropdown()
    print("✅ Dropdown test passed.")

    test_login()
    print("✅ Login test passed.")

    test_alerts()
    print("✅ Alerts test passed.")

    test_dynamic_loading()
    print("✅ Dynamic loading test passed.")

finally:
    driver.quit()
