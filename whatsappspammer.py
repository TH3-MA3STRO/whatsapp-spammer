from selenium import webdriver

import time

count = int(input("Enter the number of msgs you wnat to spam: "))
msg = input('Enter the msg you wnat to spam:')
type_ch = input("Please specify the type of chat i.e. Group or a Contact: ").lower()

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

time.sleep(20)  # Can be changed according to user's internet speed

print('count complete')
if type_ch == "contact":
    con_name = input("input contact name properly: ")
    ''' note: can only select the contact which is shown on the first screen, if you want select any other contact then 
    please scroll till you see that contact
    '''
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='_25Ooe']/span[@class='_3TEwt']/span[@title='{}']".format(con_name)).click()

elif type_ch == "group":
    g_name = input("input Group's name properly: ")
    ''' note: can only select the group which is shown on the first screen, if you want select any other group then 
    please scroll till you see that contact
    '''
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='_25Ooe']/span[@title='{}']".format(g_name)).click()

for i in range(0, count):
    driver.find_element_by_xpath("//div[@class='_2S1VP copyable-text selectable-text']").send_keys(msg)
    time.sleep(1)

    driver.find_element_by_xpath("//button[@class='_35EW6']/span").click()
    time.sleep(1)
