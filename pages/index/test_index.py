#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-09-22 19:41 

# @Author : liumengjia

# @File : test_index.py

# @Software: PyCharm

from common import basePage,data_enc
from selenium import webdriver
import pytest


locator,text,parameters = data_enc.test_get_data()
parametrize = [(locator,text,parameters)]

print(parametrize)
print(type(parametrize))
# print(len(parametrize))
# print(locator)
# print(len(locator))
# print(text)
# print(len(text))
# print(parameters)
# print(len(parameters))

class test_IndexPage(basePage.BasePage):

    ''' 统一登录url'''
    url = 'https://mobile-hwdev.jtmm.com/globalPC/#/'

    # @pytest.mark.parametrize('locator,text,parameters',[(locator[0],text[0],parameters[0]),(locator[1],text[1],parameters[1]),(locator[2],text[2],parameters[2])])
    @pytest.mark.parametrize('locator,text,parameters',parametrize)
    def test_search(self):
        self.get(self.url)

        print(locator[0])
        self.click(locator[0])

        print(locator[1])
        print(text[1])
        self.sendKeys(locator[1],text[1])

        print(locator[2])
        self.click(locator[2])

if __name__ == '__main__':

    driver = webdriver.Chrome()
    index = test_IndexPage(driver)
    index.test_search()