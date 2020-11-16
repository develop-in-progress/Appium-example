import pathlib
import os

app_path = os.path.join(str(pathlib.Path().absolute()), 'Wikipedia+v2.7.50334-r-2020-11-02.apk')


class DCSamples:
    desired_capabilities_ = {
        'Android': {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "EPHNW20525021513",
            "app": app_path,
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity",
            "autoGrantPermissions": "true",

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
    app_hash = {
        "appPackage": "org.wikipedia",
        "appActivity": "org.wikipedia.settings.SettingsActivity"
    }
    # 'D:\\PyCharm\\Appium-example\\Wikipedia+v2.7.50334-r-2020-11-02.apk'
