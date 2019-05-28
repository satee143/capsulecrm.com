from Utils import utils
import time

class Integrations:
    def __init__(self,driver):
        self.driver=driver
        self.Integrations_linktext_xpath='//a[@href and contains(text(),"Integrations")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'
        self.Count_button_xpath='//a[@class="btn-primary" and text()="Configure"]'

    def Selecting_Integrations(self):
        Integrations=self.driver.find_element_by_xpath(self.Integrations_linktext_xpath)
        inttext=Integrations.text
        Integrations.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == inttext
        print('Total Avalible Configuration Buttons in the Page are:',len(self.driver.find_elements_by_xpath(self.Count_button_xpath)))