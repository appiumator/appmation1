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
    context.platform = context.config.userdata.get("platform", "SAMSUNG")
    if platform.node() == TestCapabilities.COMPUTERS.get('jenkins') and context.device == 'mobile':
        context.appium_port = str(get_free_port())
        get_appium(context)
        system_port = get_free_port()
        TestCapabilities.CAPS.get(context.platform).update({"systemPort": system_port})
        init_driver(context)
    else:
        context.driver = eval(Platform.ENV.get(context.device).get(context.platform).get("remote"))
    if "android" in context.platform:
        context.driver.switch_to.context('CHROMIUM')
    elif context.platform == "iphone":
        context.driver.switch_to.context
    else:
        context.driver.maximize_window()
    MTPHelper.browser = context.driver

def init_driver(context):
    for trial in range(7):
        try:
            context.driver = eval(TestCapabilities.ENV.get(context.device).get(context.platform).
                                  format(port=context.appium_port, caps=TestCapabilities.CAPS.get(context.platform)))
            print('{0} STABLE>>>>>>>>>'.format(context.platform))
            break
        except Exception as e:
            for error in TestCapabilities.APPIUM_WD_ERROR_MSG:
                if error in e.msg:
                    print('{error} occured while checing {device} I am trying again!'.format(
                        error=error, device=context.platform))
                    time.sleep(randint(1, 5))
            else:
                context.subprocess.send_signal(signal.SIGINT)
                if 'Unknown device or simulator UDID' in e.msg:
                    raise ValueError('{0}is taken out from platform'.format(context.platform))
                else:
                    raise ValueError('UNKNOWN ERROR OCCURED WHILE CHECKING {0}: '.format(context.platform) + e.msg)

    else:
        print("Unstable devices {0}".format(context.platform))
        context.subprocess.send_signal(signal.SIGINT)
        raise ValueError('{0} is connected but after 7 attempts {0} is not answering'.format(context.platform))


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

