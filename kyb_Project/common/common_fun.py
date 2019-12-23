#coding:utf-8
from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging.config
from selenium.webdriver.common.by import By
import os
import time
import csv

class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    #登陆后广告取消按钮
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')
    def check_updateBtn(self):
        logging.info('===================check updateBtn===================')
        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('update element is not found')
        else:
            logging.info('click cancelBtn')
            element.click()
    def check_skipBtn(self):
        logging.info('===================check skipBtn===================')
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skip element is not found')
        else:
            logging.info('click skipBtn')
            element.click()
    def get_screenSize(self):
        '''
        :return:屏幕尺寸
        '''
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_window_size()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0], *0.95)
        x2 = int(l[0], *0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        impage_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' %(time, module)
        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(impage_file)

    def check_market_ad(self):
        '''
        检测登陆护着注册之后的界面浮窗广告
        :return:
        '''
        logging.info('===================check market ad===================')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self, csv_file, line):
        '''
        获取CSV文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        :return:
        '''
        with open(csv_file, 'r' ,encoding='utf-8-sig') as file:
            reader = csv.reader(file)
        for index, row in enumerate(reader, 1):
            if index == line:
                return row
if __name__ == '__main__':
    driver=appium_desired()

