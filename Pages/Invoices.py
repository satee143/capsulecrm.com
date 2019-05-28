from Utils import utils
import time

class Invoices:
    def __init__(self,driver):
        self.driver=driver
        self.Invoices_linktext_xpath='//a[@href and contains(text(),"Invoices")]'
        self.DisplayHeader_text_xpath='//*[@class="page-box-header"]'


    def Selecting_Invoices(self):
        Invoices=self.driver.find_element_by_xpath(self.Invoices_linktext_xpath)
        InvoiceText=Invoices.text
        Invoices.click()
        assert self.driver.find_element_by_xpath(self.DisplayHeader_text_xpath).text == InvoiceText

