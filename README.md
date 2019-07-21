# whatsapp-spammer
Spam your whatsapp groups and contacts with hundreds of messages.

###### Prerequisites:

> Latest python version 3.7

> A Terminal of course xD

###### How to install:

``` 
git clone -b 1.1_linux --single-branch https://github.com/th3-ma3stro/whatsapp-spammer.git


cd whatsapp-spammer
```

###### Required Packages

Before running the script you need these packages installed.

Modules|
:---:|
selenium-webdriver|
pyautogui|
pyfiglet|
pyinquirer|

To install these modules run while in the whatsapp-spammer directory
```
pip install -r requirements.txt
```

After that just run `python spammerli.py` and follow the on-screen instructions.
To reset login credentials just logout from your device.

### Note:
`chromedriver` should be in PATH, else mention the location of `chromedriver`

For example
```
driver = driver.Chrome(executable_path=r'''/path/to/chromedriver''')
```




