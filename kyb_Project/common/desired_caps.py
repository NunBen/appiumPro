import yaml
import logging.config
from appium import webdriver
import os

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

def appium_desired():
    with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, yaml.FullLoader)

    desird_caps = {}
    desird_caps['platformName'] = data['platformName']
    desird_caps['platformVersion'] = data['platformVersion']
    desird_caps['deviceName'] = data['deviceName']

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appname'])
    desird_caps['app'] = app_path

    desird_caps['noReset'] = data['noReset']
    desird_caps['appPackage'] = data['appPackage']
    desird_caps['appActivity'] = data['appActivity']
    print(desird_caps)
    logging.info('start run app ...')
    command_executor = 'http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub'
    driver = webdriver.Remote(command_executor,desird_caps)
    # driver.implicitly_wait(5)
    return driver

if __name__ == '__main__':
    appium_desired()
