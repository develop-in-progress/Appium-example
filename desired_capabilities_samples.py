import pathlib
import os

app_path = os.path.join(str(pathlib.Path().absolute()), 'Wikipedia.apk')


class DCSamples:
    desired_capabilities_ = {
        'android_emulator_local': {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "Android GoogleAPI Emulator",
            "app": app_path,
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "autoGrantPermissions": "true"
        },
        # 'android_saucelab_emulator': {
        #     "platformName": "Android",
        #     "platformVersion": "11",
        #     "deviceName": "Android GoogleAPI Emulator",
        #     "appiumVersion": "1.17.1",
        #     "app": "https://github.com/develop-in-progress/Appium-example/raw/main/Wikipedia.apk",
        #     "appPackage": "org.wikipedia",
        #     "appActivity": ".main.MainActivity",
        #     "autoGrantPermissions": "true",
        #     "username": os.environ['SAUCE_USERNAME'],
        #     "accessKey": os.environ['SAUCE_ACCESS_KEY'],
        #     "name": "Android tests",
        #     "deviceOrientation": "portrait",
        # },

        'ios_emulator_local': {
            "deviceName": "iPhone 11",
            "platformName": "iOS",
            "platformVersion": "14.0",
            "app": "/Users/vermilion-gym/Downloads/Wikipedia.app"
            # "automationName": "XCUITest"
            # "xcodeOrgId": "",
            # "xcodeSighingId": "iPhone Developer"
        },
        # 'ios_saucelab_emulator': {
        #     "appiumVersion": "1.17.1",
        #     "deviceOrientation": "portrait",
        #     "platformName": "iOS",
        #     "platformVersion": "13.0",
        #     "deviceName": "iPhone 11 Pro Simulator",
        #     "app": "https://github.com/develop-in-progress/Appium-example/raw/main/Wikipedia.app.zip",
        #     "browserName": "",
        #     'username': os.environ['SAUCE_USERNAME'],
        #     'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        #     "name": "iOS tests",
        #     "automationName": "XCUITest"
        # },
    }
