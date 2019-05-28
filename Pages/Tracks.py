from Utils import utils
import time

class Tracks:
    def __init__(self,driver):
        self.driver=driver
        self.Tracks_linktext_xpath='//a[@href and contains(text(),"Tracks")]'
        self.DisplayHeader_text_xpath='//*[@class="settings-page-header"]'
        self.Addtrack_button_xpath='//a[text()="Add new Track"]'
        self.Name_text_id='j_id123:trackDescriptionDecorate:trackDescription'
        self.task_text_id='j_id123:taskLines:0:taskDescriptionDecorate:taskDescription'
        self.Save_button_xpath='//a[text()="Save"]'
        self.Displayname_linktext_xpath='//a[text()="'+utils.Name+'"]'

    def Selecting_Tracks(self):
        Tracks=self.driver.find_element_by_xpath(self.Tracks_linktext_xpath)
        Tracktext=Tracks.text
        time.sleep(5)
        Tracks.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == Tracktext
        self.driver.find_element_by_xpath(self.Addtrack_button_xpath).click()
        self.driver.find_element_by_id(self.Name_text_id).send_keys(utils.Name)
        self.driver.find_element_by_id(self.task_text_id).send_keys('Hello')
        self.driver.find_element_by_xpath(self.Save_button_xpath).click()
        assert utils.Name==self.driver.find_element_by_xpath(self.Displayname_linktext_xpath).text




