import pathlib
import os

app_path = os.path.join(str(pathlib.Path().absolute()), 'Wikipedia.apk')


class DCSamples:
    desired_capabilities_ = {
        'Android': {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Android GoogleAPI Emulator",
            "app": app_path,
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "autoGrantPermissions": "true",
            'username': os.environ['SAUCE_USERNAME'],
            'accessKey': os.environ['SAUCE_ACCESS_KEY']
        },

        'Android saucelab': {
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
            "platformName": "Android",
            "platformVersion": "11",
            "deviceName": "Android Emulator",
            "app": app_path,
            "appPackage": "org.wikipedia",
            "appActivity": "org.wikipedia.settings.SettingsActivity",
            "autoAcceptAlerts": "true"
        }
    }
