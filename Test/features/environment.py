from random import randint
from sys import platform

import signal

import time

import subprocess
from selenium import webdriver as desktop_driver
from appium import webdriver as mobile_driver

from Test.TestCapabilities import TestCapabilities
from Test.PageObject.Objects.CommonPageObject import CommonPageObject
from Test.Platform import Platform
from common.Helpers.MTPHelper import MTPHelper


def before_all(context):
    context.device = context.config.userdata.get("device", "mobile")
    context.platform = context.config.userdata.get("platform", "android7")
    if platform.node() == TestCapabilities.COMPUTERS.get('jenkins') and context.device == 'mobile':
        context.appium_port = str(get_free_port())
        get_appium(context)
        system_port = get_free_port()
        TestCapabilities.CAPS.get(context.platform).update({"systemPort": system_port})
        context.driver = eval(Platform.ENV.get(context.device).get(context.platform).get("jenkins"))
    else:
        context.driver = eval(Platform.ENV.get(context.device).get(context.platform).get("remote"))
    if "android" in context.platform:
        context.driver.switch_to.context('CHROMIUM')
    elif context.platform == "iphone":
        context.driver.switch_to.context
    else:
        context.driver.maximize_window()
    MTPHelper.browser = context.driver

def get_appium(context):
    appium_params = TestCapabilities.APPIUM.get(context.platform).\
        format(appium_port=context.appium_port, chrome_port=randint(1000, 9999))
    context.subprocess = subprocess.Popen(appium_params, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)


def get_free_port():
    port = randint(1000, 9999)
    while try_port(port) is False:
        port = randint(1000, 9999)
    return port


def try_port(port):
    result = False
    check_port = 'lsof -i :{0}'.format(port)
    process = subprocess.Popen(check_port, shell=True, stdout=subprocess.PIPE)
    output = None
    for trial in range(5):
        try:
            time.sleep(1)
            output = str(process.stdout.readline())
            if 'COMMAND  PID' in output:
                break
        except:
            time.sleep(1)
    process.send_signal(signal.SIGINT)
    if 'COMMAND  PID' not in output:
        result = True
    return result



def after_all(context):
    context.driver.close()
    context.driver.quit()
    if context.device is "mobile":
        context.subprocess.send_signal(signal.SIGINT)

