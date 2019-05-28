from Utils import utils
import time

class TaskCategories:
    def __init__(self,driver):
        self.driver=driver
        self.TaskCategories_linktext_xpath='//a[@href and contains(text(),"Task Categories")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'
        self.Addcatgeory_button_xpath='//a[text()="Add new Category"]'
        self.Name_text_id="editCategoryForm:taskCategoryNameDecorate:taskCategoryName"
        self.Save_button_xpath='//input[@value="Save"]'
        self.Check_linktext_xpath='//td[@class=" list-column-left" and text()="'+utils.Name+'"]'


    def Selecting_TaskCategories(self):
        TaskCategories=self.driver.find_element_by_xpath(self.TaskCategories_linktext_xpath)
        Tasktext=TaskCategories.text
        TaskCategories.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == Tasktext

    def Add_New_Catgeory(self):
        self.driver.find_element_by_xpath(self.Addcatgeory_button_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_id(self.Name_text_id).send_keys(utils.Name)
        self.driver.find_element_by_xpath(self.Save_button_xpath).click()
        #assert utils.Name==self.driver.find_element_by_xpath(self.Check_linktext_xpath).text