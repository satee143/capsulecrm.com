from Pages.Loginpage import loginpage
from Pages.Dashboard import Dashboard
from Pages.Account import Account
from Pages.Appearance import Appearance
from Pages.CustomFields import CustomFields
from Pages.Export import Export
from Pages.Integrations import Integrations
from Pages.Invoices import Invoices
from Pages.Loginpage import loginpage
from Pages.MailDropBox import MailDropBox
from Pages.Opportunities import Opportunties
from Pages.Settings import Settings
from Pages.Tags import Tags
from Pages.TaskCategories import TaskCategories
from Pages.Tracks import Tracks
from Pages.Users import Users




import pytest
import time

@pytest.mark.usefixtures('setup')
class TestLogin():
    def test_login(self):
        #global driver,login
        driver=self.driver
        login=loginpage(driver)
        login.Login()
        displaypage=Dashboard(driver)
        displaypage.Login_Validation()
        displaypage.Add_person()
        displaypage.Add_case()

    def test_selection(self):
        self.driver.implicitly_wait(10)
        #global driver,login
        driver=self.driver
        login=loginpage(driver)
        login.Login()
        displaypage=Dashboard(driver)
        displaypage.Login_Validation()
        settings=Settings(driver)
        settings.Click_On_User_Settings()
        account=Account(driver)
        account.Selecting_Account()
        invoices=Invoices(driver)
        invoices.Selecting_Invoices()
        export=Export(driver)
        export.Selecting_Export()
        appearance=Appearance(driver)
        appearance.Selecting_Appearance()
        appearance.Uploading_Logo()
        maildropbox=MailDropBox(driver)
        maildropbox.Selecting_MailDropBox()
        users=Users(driver)
        users.Selecting_Users()
        users.Adding_User()
        opprotunties=Opportunties(driver)
        opprotunties.Selecting_Opportunities()
        opprotunties.Add_New_Milestone()
        tracks=Tracks(driver)
        tracks.Selecting_Tracks()
        taskcat=TaskCategories(driver)
        taskcat.Selecting_TaskCategories()
        taskcat.Add_New_Catgeory()
        customfields=CustomFields(driver)
        customfields.Selecting_CustomFields()
        tags=Tags(driver)
        tags.Selecting_Tags()
        tags.Adding_New_Tag()
        intigrations=Integrations(driver)
        intigrations.Selecting_Integrations()





