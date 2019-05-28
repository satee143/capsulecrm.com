from Utils import utils
import time

class Users:
    def __init__(self,driver):
        self.driver=driver
        self.Users_linktext_xpath='//a[@href and contains(text(),"Users")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'
        self.Adduser_button_xpath='//a[text()="Add new User"]'
        self.Firstname_text_xpath='//input[@id="register:firstnameDecorate:firstName"]'
        self.Lastname_text_xpath = '//input[@id="register:lastNameDecorate:lastName"]'
        self.Email_text_xpath = '//input[@id="register:emailDecorate:email"]'
        self.Username_text_xpath = '//input[@id="register:usernameDecorate:username"]'
        self.Inviteuser_button_xpath='//input[@id="register:save"]'
        self.CheckUser_text_xpath='//td[contains(text(),"'+utils.UName+'"]'

    def Selecting_Users(self):
        Users=self.driver.find_element_by_xpath(self.Users_linktext_xpath)
        UserText= Users.text
        Users.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text ==UserText


    def Adding_User(self):
        self.driver.find_element_by_xpath(self.Adduser_button_xpath).click()
        self.driver.find_element_by_xpath(self.Firstname_text_xpath).send_keys(utils.FName)
        self.driver.find_element_by_xpath(self.Lastname_text_xpath).send_keys(utils.LName)
        self.driver.find_element_by_xpath(self.Email_text_xpath).send_keys(utils.EmaiL)
        self.driver.find_element_by_xpath(self.Username_text_xpath).send_keys(utils.UName)
        self.driver.find_element_by_xpath(self.Inviteuser_button_xpath).click()
        #assert utils.UName==self.driver.find_element_by_xpath(self.CheckUser_text_xpath).text ##### CHECK THIS ONE


