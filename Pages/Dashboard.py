from Utils import utils
from selenium.webdriver.support.select import Select
import time
class Dashboard:
    def __init__(self,driver):
        self.driver=driver
        self.DisplayName_text_class = 'nav-bar-username'
        self.People_imagelink_xpath='//a[@aria-label="People & Organisations"]'
        self.Addperson_textlink_xpath='//a[text()="Add Person"]'
        self.Title_Dropdown_name='party:j_id108:j_id116'
        self.Firstname_textbox_name='party:fnDecorate:fn'
        self.Lastname_textbox_name='party:lnDecorate:ln'
        self.Jobtitle_textbox_name='party:roleDecorate:jobTitle'
        self.Orgnization_textbox_name='party:orgDecorate:org'
        self.Tag_textbox_name='party:tagsDecorate:tagComboBox'
        self.Addtag_button_name='party:tagsDecorate:j_id187'
        self.Phonenumber_textbox_name='party:j_id325:0:phnDecorate:number'
        self.Email_textbox_name='party:j_id342:0:emlDecorate:nmbr'
        self.Save_button_name='party:save'
        self.DisplayedName_text_xpath='//span[@class="party-details-title"]'
        self.Cases_imagelink_xpath='//a[@aria-label="Cases"]'
        self.Addcase_textlink_xpath='//a[text()="Add Case"]'
        self.Party_text_id='partySearch'
        self.Related_link_xpath='//li[contains(text(),"Dusa")]'
        self.Casename_text_id='caseNameDecorate:name'
        self.Savecase_button_id='save'
        self.Entity_text_xpath='//div[@class="entity-details-title"]'
        self.Person_text_xpath='//a[@class="ember-view"]'
        self.Casestatus_text_xpath='//span[@class="kase-summary-status-open"]'




    def Login_Validation(self):
        DisplayName=self.driver.find_element_by_class_name(self.DisplayName_text_class).text
        assert DisplayName==utils.DisplayName

    def Add_person(self):
        self.driver.find_element_by_xpath(self.People_imagelink_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.Addperson_textlink_xpath).click()
        Select(self.driver.find_element_by_name(self.Title_Dropdown_name)).select_by_visible_text('Mr')
        self.driver.find_element_by_name(self.Firstname_textbox_name).send_keys(utils.First_Name)
        self.driver.find_element_by_name(self.Lastname_textbox_name).send_keys(utils.Last_Name)
        self.driver.find_element_by_name(self.Jobtitle_textbox_name).send_keys(utils.Job_Title)
        self.driver.find_element_by_name(self.Orgnization_textbox_name).send_keys(utils.Orgnization)
        self.driver.find_element_by_name(self.Tag_textbox_name).send_keys(utils.Tags)
        self.driver.find_element_by_name(self.Addtag_button_name).click()
        time.sleep(5)
        self.driver.find_element_by_name(self.Phonenumber_textbox_name).send_keys(utils.Phone_Number)
        self.driver.find_element_by_name(self.Email_textbox_name).send_keys(utils.Email)
        time.sleep(3)
        self.driver.find_element_by_name(self.Save_button_name).click()
        time.sleep(1)
        Displayed_Name=self.driver.find_element_by_xpath(self.DisplayedName_text_xpath).text
        assert Displayed_Name == utils.DisplayedName

    def Add_case(self):
        self.driver.find_element_by_xpath(self.Cases_imagelink_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.Addcase_textlink_xpath).click()
        self.driver.find_element_by_id(self.Party_text_id).send_keys(utils.First_Name)
        time.sleep(10)
        self.driver.find_element_by_xpath(self.Related_link_xpath).click()
        self.driver.find_element_by_id(self.Casename_text_id).send_keys(utils.Casename)
        time.sleep(6)
        self.driver.find_element_by_id(self.Savecase_button_id).click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(self.Entity_text_xpath).text == utils.Casename
        assert self.driver.find_element_by_xpath(self.Person_text_xpath).text ==utils.CaseDisplayedName
        assert self.driver.find_element_by_xpath(self.Casestatus_text_xpath).text == 'Open'
