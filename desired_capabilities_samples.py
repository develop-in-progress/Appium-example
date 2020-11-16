import pathlib
import os


app_path = os.path.join(str(pathlib.Path().absolute()), 'Wikipedia+v2.7.50334-r-2020-11-02.apk')


class DCSamples:
    desired_capabilities_virtual_pixel2 = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "app": app_path,
            # "D:\\PyCharm\\Appium-example\\Wikipedia+v2.7.50334-r-2020-11-02.apk", comment for Appium server
        "appPackage": "org.wikipedia",
        "appActivity": ".main.MainActivity",
        }

