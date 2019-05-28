from Utils import utils
import time


class CustomFields:
    def __init__(self,driver):
        self.driver=driver
        self.CustomFields_linktext_xpath='//a[@href and contains(text(),"Custom Fields")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'

    def Selecting_CustomFields(self):
        CustomFields=self.driver.find_element_by_xpath(self.CustomFields_linktext_xpath)
        Customtext=CustomFields.text
        time.sleep(5)
        CustomFields.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == Customtext