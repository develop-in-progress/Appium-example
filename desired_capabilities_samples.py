import pathlib
import os

app_path = os.path.join(str(pathlib.Path().absolute()), 'Wikipedia.apk')


class DCSamples:
    desired_capabilities_ = {
        'Android': {
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "Android GoogleAPI Emulator",
            "app": app_path,
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "autoGrantPermissions": "true"
        },

<<<<<<< HEAD
        # 'Android Saucelab': {
        #     "platformName": "Android",
        #     "platformVersion": "10",
        #     "deviceName": "Android GoogleAPI Emulator",
        #     "appiumVersion": "1.17.1",
        #     "app": "https://github.com/develop-in-progress/Appium-example/raw/saucelab_test/Wikipedia.apk",
        #     "appPackage": "org.wikipedia",
        #     "appActivity": ".main.MainActivity",
        #     "autoGrantPermissions": "true",
        #     "username": os.environ['SAUCE_USERNAME'],
        #     "accessKey": os.environ['SAUCE_ACCESS_KEY'],
        #     "name": "first tests",
        #     "deviceOrientation": "portrait",
        # },

        # 'iOS': {
        #     "deviceName": "iPhone 11",
        #     "platformName": "iOS",
        #     "platformVersion": "14.0",
        #     "app": "/Users/vermilion-gym/Downloads/Wikipedia.app"
        # },
        # 'iOS': {
        #     "deviceName": "iPhone 11",
        #     "platformName": "iOS",
        #     "platformVersion": "14.0",
        #     "app": "/Users/vermilion-gym/Downloads/Wikipedia.app",
        #     "automationName": "XCUITest"
        #     # "xcodeOrgId": "",
        #     # "xcodeSighingId": "iPhone Developer"
        # },
        'iOS': {
            "deviceName": "G5_TEST",
            "platformName": "iOS",
            "platformVersion": "13.1.2",
            "udid": "00008020-00064D9C0C02003A",
            "app": "/Users/vermilion-gym/Library/Developer/Xcode/DerivedData/Wikipedia-cagwciwcxgkdfhcptnywdmtfkpfu/Build/Products/Debug-iphoneos/Wikipedia.app",
            "automationName": "XCUITest"
        },
        # 'iOS Saucelab': {
        #     "appiumVersion": "1.17.1",
        #     "deviceOrientation": "portrait",
        #     "platformName": "iOS",
        #     "platformVersion": "13.0",
        #     "deviceName": "iPhone 11 Pro Simulator",
        #     "app": "https://github.com/develop-in-progress/Appium-example/raw/saucelab_test/Wikipedia.app.zip",
        #     "browserName": "",
        #     'username': os.environ['SAUCE_USERNAME'],
        #     'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        #     "automationName": "XCUITest"
        #
        # }
=======
        'Android Saucelab': {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Android GoogleAPI Emulator",
            "appiumVersion": "1.17.1",
            "app": "https://github.com/develop-in-progress/Appium-example/raw/saucelab_test/Wikipedia.apk",
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "autoGrantPermissions": "true",
            "username": os.environ['SAUCE_USERNAME'],
            "accessKey": os.environ['SAUCE_ACCESS_KEY'],
            "name": "first tests",
            "deviceOrientation": "portrait",
        },

        'iOS': {
            "appiumVersion": "1.17.1",
            "deviceOrientation": "portrait",
            "platformName": "iOS",
            "platformVersion": "13.0",
            "deviceName": "iPhone 11 Pro Simulator",
            "app": "https://github.com/develop-in-progress/Appium-example/raw/saucelab_test/Wikipedia.app.zip",
            "browserName": "",
            "automationName": "XCUITest"
        },
        'iOS Saucelab': {
            "appiumVersion": "1.17.1",
            "deviceOrientation": "portrait",
            "platformName": "iOS",
            "platformVersion": "13.0",
            "deviceName": "iPhone 11 Pro Simulator",
            "app": "https://github.com/develop-in-progress/Appium-example/raw/saucelab_test/Wikipedia.app.zip",
            "browserName": "",
            'username': os.environ['SAUCE_USERNAME'],
            'accessKey': os.environ['SAUCE_ACCESS_KEY'],
            "automationName": "XCUITest"

        }
>>>>>>> apple_testing
    }
