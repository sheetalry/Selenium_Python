
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

 
opt=Options()
#opt.headless=True
opt.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://landing.svcs.bluesky.tmc-dev.cloud.vmware.com/landing?stack=tap-sc-ga&orgLink=/csp/gateway/am/api/orgs/bc27608b-4809-4cac-9e04-778803963da2")
print("App title ",driver.title)
time.sleep(10)
driver.implicitly_wait(15)
driver.save_screenshot("test.png")

driver.quit()