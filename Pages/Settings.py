from Utils import utils
import time

class Settings:
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)
        self.Usermenu_linktext_xpath='//span[@class="nav-bar-username"]'
        self.Accountsettings_linktext_xpath='//a[text()="Account Settings"]'
        self.Diplayedmenu_text_xpath='//span[@class="settings-content-menu-title"]'

    def Click_On_User_Settings(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.Usermenu_linktext_xpath).click()
        Account_setting=self.driver.find_element_by_xpath(self.Accountsettings_linktext_xpath)
        Account_Settings = Account_setting.text
        Account_setting.click()
        Displayed_text=self.driver.find_element_by_xpath(self.Diplayedmenu_text_xpath).text
        assert Account_Settings == Displayed_text
