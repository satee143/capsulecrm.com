from Utils import utils
import time

class MailDropBox:
    def __init__(self,driver):
        self.driver=driver
        self.MailDropBox_linktext_xpath='//a[@href and contains(text(),"Mail Drop Box")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'

    def Selecting_MailDropBox(self):
        MailDropBox=self.driver.find_element_by_xpath(self.MailDropBox_linktext_xpath)
        MailDropText=MailDropBox.text
        MailDropBox.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == MailDropText