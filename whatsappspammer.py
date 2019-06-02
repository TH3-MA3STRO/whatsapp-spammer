# imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# user inputs
count = int(input("Enter the number of messages you want to spam: "))
msg = input('Enter the message you want to spam: ')
type_ch = input("Please specify the type of chat (i.e. Group or a Contact): ").lower()
# script
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

time.sleep(10)  # Can be changed according to user's internet speed

print('count complete')
if type_ch == "contact":
    con_name = input("input contact name properly: ")

    time.sleep(2)
    ActionChains(driver).move_to_element(driver.find_element_by_xpath(
        "//div[@class='_25Ooe']/span[@class='_3TEwt']/span[@title='{}']".format(con_name)).click()
    )


elif type_ch == "group":
    g_name = input("input Group's name properly: ")

    time.sleep(2)
    ActionChains(driver).move_to_element(
        driver.find_element_by_xpath("//div[@class='_25Ooe']/span[@title='{}']".format(g_name)).click())

for i in range(0, count):
    driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']").send_keys(msg)
    time.sleep(1)

    driver.find_element_by_xpath("//button[@class='_35EW6']/span").click()
    time.sleep(1)

print("Script Complete! ")
time.sleep(6)
driver.__exit__()
