from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("D:\chromedriver\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service = serv_obj, options=options)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
submit_button = driver.find_element(By. XPATH, "//button[@type='submit']")


username_field.send_keys("Admin")
password_field.send_keys("admin123")
submit_button.click()

dashboard_text = driver.find_element(By. XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
if dashboard_text.is_displayed():
    print("Test passed")
else:
    print("Test failed")



