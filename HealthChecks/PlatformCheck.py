import signal
import socket
import subprocess
import time
from random import randint

import sys
from appium import webdriver as mobile_driver


device = str(sys.argv[1])


def get_free_port():
    port = randint(1000, 9999)
    while try_port(port) is False:
        port = randint(1000, 9999)
    return port


def try_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind(("0.0.0.0", port))
        result = True
    except:
        print("Port is in use")
    sock.close()
    return result


APPIUM = {
    "LG": "appium -p {appium_port} --chromedriver-port {chrome_port}",
    "XIAOMI": "appium -p {appium_port} --chromedriver-port {chrome_port}",
    "SAMSUNG": "appium -p {appium_port} --chromedriver-port {chrome_port}",
    "IPHONE": "appium -p {appium_port} --chromedriver-port {chrome_port}"
}

CAPS = {
    "LG": {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': 'Android',
        'browserName': 'Chrome',
        'skipUnlock': False,
        'clearSystemFiles': True,
        'automationName': 'UiAutomator2',
        "udid": "31005dd5362eb2e1"
    },
    "XIAOMI": {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'Android',
        'browserName': 'Chrome',
        'skipUnlock': False,
        'clearSystemFiles': True,
        'automationName': 'UiAutomator2',
        "udid": "LGM160236696d9"
    },
    "SAMSUNG": {
        'platformName': 'Android',
        'platformVersion': '7.1.2',
        'deviceName': 'Android',
        'browserName': 'Chrome',
        'skipUnlock': False,
        'clearSystemFiles': True,
        'automationName': 'UiAutomator2',
        "udid": "4ff3743c0904"
    },
    ""
    "IPHONE": {
        'platformName': 'iOS',
        'platformVersion': '12.0',
        'deviceName': 'iPhone (Perform)',
        'clearSystemFiles': True,
        'automationName': 'XCUITest',
        "autoWebview": True,
        "startIWDP": True,
        "app": "",
        'browserName': 'Safari',
        "udid": "02d1d609384136060123cf2bbfa46faf72d2ccc1",
        "showXcodeLog": True
    }
}

ENV = {
        "XIAOMI": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})",
        "SAMSUNG": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})",
        "LG": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})",
        "IPHONE": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})"

}

APPIUM_WD_ERROR_MSG = ["is already in use", 'ECONNREFUSED', '[Errno 61] Connection refused']

appium_port = get_free_port()
appium_params = APPIUM.get(device).format(appium_port)
process = subprocess.Popen(appium_params, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(4)
system_port = get_free_port()
CAPS.get(device).update({"systemPort": system_port})
for trial in range(7):
    try:
        eval(ENV.get(device).format(port=appium_port, caps=CAPS.get(device)))
        print('{0} STABLE>>>>>>>>>'.format(device))
        process.send_signal(signal.SIGINT)
        break
    except Exception as e:
        for error in APPIUM_WD_ERROR_MSG:
            if error in e.msg:
                print('{error} occured while checing {device}I am trying again!'.format(error=error, device=device))
                time.sleep(randint(1, 5))
        else:
            process.send_signal(signal.SIGINT)
            if 'Unknown device or simulator UDID' in e.msg:
                raise ValueError('{0} is taken out from platform'.format(device))
            else:
                raise ValueError('UNKNOWN ERROR OCCURED WHILE CHECKING {0}: '.format(device) + e.msg)

else:
    print("Unstable devices {0}".format(device))
    process.send_signal(signal.SIGINT)
    raise ValueError('{0} is connected but after 7 attempts {0} is not answering'.format(device))
