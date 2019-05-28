from Utils import utils

import time

class Account:
    def __init__(self,driver):
        self.driver=driver
        self.Account_linktext_xpath='//a[text()="Account"]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'

    def Selecting_Account(self):
        Account=self.driver.find_element_by_xpath(self.Account_linktext_xpath)
        AccountText=Account.text
        Account.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == AccountText