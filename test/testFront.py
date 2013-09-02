#coding=UTF-8

__author__ = 'wanghongmeng'

from service import frontService

def testCatagoryName():
    catagoryNames = frontService.getCatagoryName()
    for catagoryName in catagoryNames:
        print catagoryName


if __name__ == "__main__":
    testCatagoryName()

