from selenium import webdriver as desktop_driver
from appium import webdriver as mobile_driver
from Test.PageObject.Objects.CommonPageObject import CommonPageObject
from Test.Platform import Platform
from common.Helpers.MTPHelper import MTPHelper


def before_all(context):
    context.device = context.config.userdata.get("device", "mobile")
    context.platform = context.config.userdata.get("platform", "android7")
    context.driver = eval(Platform.ENV.get(context.device).get(context.platform))
    if "android" in context.platform:
        context.driver.switch_to.context('CHROMIUM')
    elif context.platform == "iphone":
        context.driver.switch_to.context
    else:
        context.driver.maximize_window()


def after_all(context):
    context.driver.close()
    context.driver.quit()
