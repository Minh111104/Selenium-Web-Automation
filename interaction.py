from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# narrow down to the anchor tag using CSS Selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

# find element by Link
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# sending keyboard input to selenium
# search.send_keys("Python")
search.send_keys("Python", Keys.ENTER)

