from Utils import utils
import time

class Appearance:
    def __init__(self,driver):
        self.driver=driver
        self.Appearance_linktext_xpath='//a[@href and contains(text(),"Appearance")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'
        self.Uploadlogo_button_id="appearance:uploadDecorate:logoImage"
        self.Save_button_xpath='//a[text()="Save"]'

    def Selecting_Appearance(self):
        Appearance=self.driver.find_element_by_xpath(self.Appearance_linktext_xpath)
        AppearanceText=Appearance.text
        Appearance.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == AppearanceText
    def Uploading_Logo(self):
        time.sleep(5)
        self.driver.find_element_by_id(self.Uploadlogo_button_id).send_keys(utils.logopath)
        assert self.driver.find_element_by_id(self.Uploadlogo_button_id).text in utils.logopath
        self.driver.find_element_by_xpath(self.Save_button_xpath).click()
