
import time

from Test.PageObject.Elements.CommonPageElement import CommonPageElement
from common.Helpers.MTPHelper import MTPHelper
from selenium.webdriver.common.keys import Keys



class CommonPageObject(CommonPageElement):
    def __init__(self, context):
        MTPHelper.browser = context.driver

    def open(self, domain):
        MTPHelper.open(self.URLs.get(domain))

    def search_for(self, keyword):
        MTPHelper.type(self.LOCATORS.get("search box"), keyword)
        MTPHelper.type(self.LOCATORS.get("search box"), Keys.RETURN)
        time.sleep(2) # just to be able to see the results
