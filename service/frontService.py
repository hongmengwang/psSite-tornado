#coding=UTF-8
__author__ = 'wanghongmeng'

from db import datasource

pool = datasource.initDBPool()

def getCatagoryName():
    catagoryNames = datasource.query(pool,"select * from catagory_name")
    return catagoryNames