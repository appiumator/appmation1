class Platform:

    CAPS_ANDROID_7 = {
        'platformName': 'Android',
        'platformVersion': '7.1.2',
        'deviceName': 'Android',
        'browserName': 'Chrome',
        'skipUnlock': False,
        'clearSystemFiles': True,
        'automationName': 'UiAutomator2',
        "udid": "4ff3743c0904",
        "systemPort": 1117
    }

    CAPS_ANDROID_6 = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',
        'deviceName': 'Android',
        'browserName': 'Chrome',
        'skipUnlock': False,
        'clearSystemFiles': True,
        'automationName': 'UiAutomator2',
        "udid": "LGM160236696d9",
        "systemPort": 1116
    }

    CAPS_ANDROID_5 = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': 'Android',
        'browserName': 'Chrome',
        'skipUnlock': False,
        'clearSystemFiles': True,
        'automationName': 'UiAutomator2',
        "udid": "31005dd5362eb2e1",
        "systemPort": 1115
    }

    CAPS_IPHONE = {
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
        "showXcodeLog": True,
        "systemPort": 1110
    }


    ENV = {
        "mobile": {
            "android6": "mobile_driver.Remote('http://10.216.99.56:4726/wd/hub', {})".format(CAPS_ANDROID_6),
            "android7": "mobile_driver.Remote('http://10.216.99.56:4727/wd/hub', {})".format(CAPS_ANDROID_7),
            "android5": "mobile_driver.Remote('http://10.216.99.56:4725/wd/hub', {})".format(CAPS_ANDROID_5),
            "iphone": "mobile_driver.Remote('http://10.216.99.56:4720/wd/hub', {})".format(CAPS_IPHONE)
        },
        "desktop": {
            "safari": "desktop_driver.Safari()",
            "chrome": "desktop_driver.Chrome()",
            "firefox": "desktop_driver.Firefox()",
            "ie": "desktop_driver.Ie()"
        }
    }
