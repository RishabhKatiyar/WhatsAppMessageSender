import webbrowser as web
from urllib.parse import quote
import pyautogui as pg
import pywhatkit
import time
import sys

class custom_py_what_kit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sendwhatmsg_instantly(self, phone_no, message, wait_time=20, browser=None) -> None:
        
        if browser and browser.lower() not in ["chrome", "firefox", "brave", "opera"]:
            raise InvalidBrowserName("Browser name can be firefox, chrome, brave, opera")

        if "+" not in phone_no:
            raise CountryCodeException("Country code missing from phone_no")
        
        parsedMessage = quote(message)
        web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
        time.sleep(2)
        width,height = pg.size()
        if browser:
            whats = pg.getWindowsWithTitle(browser)[0]
            whats.maximize()
            whats.activate()
        pg.click(width/2,height/2)
        time.sleep(wait_time-2)
        
        # print('Closing previous tab..')
        # pg.hotkey('ctrl', 'shift', 'tab')
        # pg.hotkey('ctrl', 'w',)
        
        pg.moveTo(self.x, self.y)
        pg.click()
        pg.press('right')
        pg.press('enter')
        
        time.sleep(1)

        print('Closing Current Tab .. ')
        pg.hotkey('ctrl', 'w',)