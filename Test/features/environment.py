# from appium import webdriver
from selenium import webdriver
from Test.PageObject.Objects.CommonPageObject import CommonPageObject
from common.Helpers.MTPHelper import MTPHelper

CAPS_ANDROID = {
    'platformName': 'Android',
    'platformVersion': '7.1.2',
    'deviceName': 'Android',
    'browserName': 'Chrome',
    'clearSystemFiles': True,
    'automationName': 'UiAutomator2',
    "udid": "4ff3743c0904",
}


def before_all(context):
    context.driver = webdriver.Remote('http://0.0.0.0:4726/wd/hub', CAPS_ANDROID)
    context.driver.switch_to.context('CHROMIUM')
    MTPHelper.browser = context.driver
    context.common = CommonPageObject(context)


def after_all(context):
    context.driver.close()
    context.driver.quit()
