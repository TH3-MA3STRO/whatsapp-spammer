# imports
from selenium import webdriver

import time

import pyautogui

# user inputs
count = int(input("Enter the number of messages you want to spam: "))

type_ch = input("Please specify the type of chat i.e. Group or a Contact: ").lower()

# script
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

time.sleep(10)  # Can be changed according to user's internet speed

if type_ch == "contact":
    con_name = pyautogui.prompt("Enter Contact's Name")
    driver.find_element_by_xpath(
        "//div[@class='ZP8RM']/label[@class='eiCXe']/input[@class='_2zCfw copyable-text selectable-text']").click()

    pyautogui.typewrite(con_name)
    time.sleep(2)

    driver.find_element_by_xpath("//span[@class='_3NWy8']/span[@class='_19RFN']/span[@class='matched-text']").click()

elif type_ch == "group":
    g_name = pyautogui.prompt("Enter Group's Name")
    driver.find_element_by_xpath("//div[@class='ZP8RM']/label[@class='eiCXe']/input[@class='_2zCfw copyable-text "
                                 "selectable-text']").click()
    pyautogui.typewrite(g_name)

    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='_2WP9Q']/div[@class='KgevS']/div[@class='_3H4MS']/span["
                                 "@class='_19RFN']/span[@class='matched-text']").click()

msg = pyautogui.prompt("Enter the msg you wish to spam")
for i in range(0, count):
    driver.find_element_by_xpath(
        "//div[@id='main']/footer[@class='_1N6pS']/div[@class='_2i7Ej copyable-area']/div[@class='_13mgZ']").click()

    time.sleep(1)

    pyautogui.typewrite(msg)

    driver.find_element_by_xpath("//div[@class='hnQHL'][2]/button[@class='_3M-N-']/span").click()

    time.sleep(1)

pyautogui.alert('The chat was bombed successfully!')

driver.__exit__()
