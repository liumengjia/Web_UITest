#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-09-24 19:49 

# @Author : liumengjia

# @File : data_enc.py 

# @Software: PyCharm

from tools.test_excel import TestExcel

def test_get_data():

    wb = TestExcel('../data/data.xlsx','IndexPage')
    data = wb.test_get_data()

    operation = [item['operation'] for item in data]
    text =      [item['text'] for item in data]
    location_type = [item['location_type'] for item in data]
    value =     [item['value'] for item in data]

    locator = list(zip(location_type, value))

    parameters = list(zip(operation,text))

    return locator,text,parameters

if __name__=='__main__':
    print(test_get_data())
