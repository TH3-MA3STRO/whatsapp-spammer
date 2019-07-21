# imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from cli import que1
import pyautogui

# user inputs

inps = que1()
type_ch = inps['tch'].lower()
count = int(inps['num'])

# driver configs
options = webdriver.ChromeOptions()
options.add_argument(r'''--user-data-dir=./User_Data''')

driver = webdriver.Chrome(options=options)
act = ActionChains(driver)
driver.get("https://web.whatsapp.com")

act = ActionChains(driver)
wait = WebDriverWait(driver, 40)
time.sleep(10)  # Can be changed according to user's internet speed

# script

try:
    if type_ch == "contact":
        con_name = pyautogui.prompt("Enter Contact's Name")
        wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='ZP8RM']/label[@class='eiCXe']/input[@class='_2zCfw copyable-text selectable-text']")))
        driver.find_element_by_xpath(
            "//div[@class='ZP8RM']/label[@class='eiCXe']/input[@class='_2zCfw copyable-text selectable-text']").send_keys(
            con_name)

        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='_3NWy8']/span[@class='_19RFN']/span["
                                                               "@class='matched-text']")))

        driver.find_element_by_xpath(
            "//span[@class='_3NWy8']/span[@class='_19RFN']/span[@class='matched-text']").click()

    elif type_ch == "group":
        g_name = pyautogui.prompt("Enter Group's Name")
        wait.until(ec.visibility_of_element_located((By.XPATH,
                                                     "//div[@class='ZP8RM']/label[@class='eiCXe']/input[@class='_2zCfw copyable-text selectable-text']")))
        driver.find_element_by_xpath("//div[@class='ZP8RM']/label[@class='eiCXe']/input[@class='_2zCfw copyable-text "
                                     "selectable-text']").send_keys(g_name)
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH,
                                                     "//div[@class='_2WP9Q']/div[@class='KgevS']/div[@class='_3H4MS']/span[@class='_19RFN']/span[@class='matched-text']")))
        driver.find_element_by_xpath("//div[@class='_2WP9Q']/div[@class='KgevS']/div[@class='_3H4MS']/span["
                                     "@class='_19RFN']/span[@class='matched-text']").click()

    msg = pyautogui.prompt("Enter the msg you wish to spam")
    for i in range(0, count):
        driver.find_element_by_xpath(
            "//div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']").send_keys(
            msg)
        time.sleep(0.25)

        driver.find_element_by_xpath("//div[@class='hnQHL'][2]/button[@class='_3M-N-']/span").click()
        time.sleep(0.5)

    pyautogui.alert('The chat was bombed successfully!')

except selenium.common.exceptions.WebDriverException:
    pyautogui.alert("Some error occurred :(")
    time.sleep(10)

driver.__exit__()
