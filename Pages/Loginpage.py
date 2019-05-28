from Utils import utils
import time
class loginpage:

    ### Object Repository
    def __init__(self,driver):
        self.driver=driver
        self.Username_textbox_id='login:usernameDecorate:username'
        self.Password_textbox_id='login:passwordDecorate:password'
        self.Login_button_id='login:login'


    ### Login to page
    def Login(self):
        self.driver.find_element_by_id(self.Username_textbox_id).send_keys(utils.username)
        self.driver.find_element_by_id(self.Password_textbox_id).send_keys(utils.password)
        self.driver.find_element_by_id(self.Login_button_id).click()


