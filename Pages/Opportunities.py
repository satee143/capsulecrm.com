from Utils import utils
import time
from selenium.webdriver.common.keys import Keys
from random_word import RandomWords



class Opportunties:
    def __init__(self, driver):
        self.driver = driver
        self.Opportunities_linktext_xpath = '//a[@href and contains(text(),"Opportunities")]'
        self.DisplayHeader_text_xpath = '//*[@class="page-box-header"]'
        self.Addnewmilestone_button_xpath='//button[text()="Add new Milestone"]'
        self.Name_text_xpath='//input[@class="form-input-text milestone-modal-name"]'
        self.Probabliity_text_xpath='//input[@class="form-input-text milestone-modal-probability"]'
        self.Save_button_xpath='//button[text()="Save"]'
        self.DisplayedName_linktext_xpath='//button[@class and text()="'+str(utils.Name)+'"]'

    def Selecting_Opportunities(self):
        Opportunities = self.driver.find_element_by_xpath(self.Opportunities_linktext_xpath)
        Opptext=Opportunities.text
        Opportunities.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == Opptext

    def Add_New_Milestone(self):
        r=RandomWords()
        name=r.get_random_word()
        self.driver.find_element_by_xpath(self.Addnewmilestone_button_xpath).click()
        self.driver.find_element_by_xpath(self.Name_text_xpath).send_keys(name)
        self.driver.find_element_by_xpath(self.Probabliity_text_xpath).send_keys('5')
        self.driver.find_element_by_xpath(self.Save_button_xpath).click()
        #assert name == self.driver.find_element_by_xpath(self.DisplayedName_linktext_xpath).text



