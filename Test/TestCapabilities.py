class TestCapabilities:
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
        "XIAOMI":{
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
        "mobile": {
            "jenkins": {
                "XIAOMI": "mobile_driver.Remote('http://localhost:{port}/wd/hub', {caps})",
                "SAMSUNG": "mobile_driver.Remote('http://localhost:{port}/wd/hub', {caps})",
                "LG": "mobile_driver.Remote('http://localhost:{port}/wd/hub', {caps})",
                "IPHONE": "mobile_driver.Remote('http://localhost:{port}/wd/hub', {caps})"
            },
            "remote": {
                "XIAOMI": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})",
                "SAMSUNG": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})",
                "LG": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})",
                "IPHONE": "mobile_driver.Remote('http://192.168.l.2:{port}/wd/hub', {caps})"
            }
        },
        "desktop": {
            "jenkins": {
                "safari": "desktop_driver.Safari()",
                "chrome": "desktop_driver.Chrome()",
                "firefox": "desktop_driver.Firefox()"
            },
            "remote":{
                "chrome": "desktop_driver.Chrome()",
                "firefox": "desktop_driver.Firefox()",
                "ie": "desktop_driver.Ie()"
            }
        }
    }

    APPIUM = {
        "LG": "appium -p {appium_port} --chromedriver-port {chrome_port}",
        "XIAOMI": "appium -p {appium_port} --chromedriver-port {chrome_port}",
        "SAMSUNG": "appium -p {appium_port} --chromedriver-port {chrome_port}",
        "IPHONE": "appium -p {appium_port} --chromedriver-port {chrome_port}"
    }

    COMPUTERS = {"jenkins": 'jenkins.local'}
