from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# find the first name, last name, email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# fill out the form
first_name.send_keys("Minh")
last_name.send_keys("Nguyen")
email.send_keys("quangminh111104@gmail.com")

# locate the "Sign Up" button. Then click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
