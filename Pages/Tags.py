from Utils import utils
import time

class Tags:
    def __init__(self,driver):
        self.driver=driver
        self.Tags_linktext_xpath='//a[@href and contains(text(),"Tags")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'
        self.Addtag_button_xpath='//a[text()="Add new Tag"]'
        self.Name_text_id="j_id177:tagNameDecorate:tagName"
        self.Save_button_xpath='//input[@value="Save"]'
        self.Check_name_xpath='//a[text()="DOOOOO"]'

    def Selecting_Tags(self):
        Tags=self.driver.find_element_by_xpath(self.Tags_linktext_xpath)
        Tagstext=Tags.text
        Tags.click()
        assert Tagstext in self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text
    def Adding_New_Tag(self):
        self.driver.find_element_by_xpath(self.Addtag_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.Name_text_id).send_keys('DOOOOO')
        self.driver.find_element_by_xpath(self.Save_button_xpath).click()
        assert self.driver.find_element_by_xpath(self.Check_name_xpath).text == "DOOOOO"

