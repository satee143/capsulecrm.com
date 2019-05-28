from Utils import utils
import time

class Export:
    def __init__(self,driver):
        self.driver=driver
        self.Export_linktext_xpath='//a[@href and contains(text(),"Export")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'

    def Selecting_Export(self):
        Export=self.driver.find_element_by_xpath(self.Export_linktext_xpath)
        ExportText= Export.text
        Export.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text ==ExportText