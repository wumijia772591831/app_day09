from appium import webdriver

def get_server_settings(package,activity):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['deviceName'] = 'sumsang'
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
