from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

from secret import username, password, artist_url

counter = 1

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('C:\selenium\chromedriver.exe')

    def Login(self):
        bot = self.bot
        bot.maximize_window()
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        bot.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB').click()
        time.sleep(1)


    def openStories(self):
        bot = self.bot
        bot.find_element_by_class_name('aOOlW.HoLwm').click()
        # stroies : c6Ldk
        time.sleep(0.5)
        # bot.find_element_by_class_name('c6Ldk').click()


    def open_followers_by_artist(self, artist_url):
        time.sleep(2)
        self.bot.get(artist_url)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click() # open followers
        time.sleep(2)

def open_story(profile):
    go.bot.execute_script("arguments[0].scrollIntoView();", profile)
    profile.click()

def close_story():
    time.sleep(1)
    close_story_btn = go.bot.find_element_by_class_name('Szr5J')
    time.sleep(1)
    close_story_btn.click()

go = InstaBot(username,password)
go.Login()
go.open_followers_by_artist(artist_url)

while True:
    profiles = go.bot.find_elements_by_class_name('h5uC0') # list of profiles
    for profile in profiles[counter:]:
        try:
            open_story(profile)
            counter += 1
            close_story()
        except Exception as e:
            # after click follower link, wait until dialog appear
            break
    time.sleep(1)
    WebDriverWait(go.bot, 10).until(lambda d: d.find_element_by_css_selector('div[role="dialog"]'))
    go.bot.execute_script('''var fDialog = document.querySelector('div[role="dialog"] .isgrP');fDialog.scrollTop = fDialog.scrollHeight''')
    print counter
    # now scroll

