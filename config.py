#coding=UTF-8
__author__ = 'hongmengwang'

import logging
import time
import MySQLdb
import os

logfile = "/home/xiaowang/PycharmProjects/psSite/logs/" + time.strftime("%Y%m%d") + ".log"
if(not os.path.exists(logfile)):
    os.mknod(logfile)
logging.basicConfig(level = logging.DEBUG,format="[%(asctime)s]:[%(name)s]:[%(levelname)s]:[%(pathname)s]:[line-number:%(lineno)d]:[%(message)s]",datefmt="%Y-%m-%d %H:%M",filename = logfile)

template_path = "/home/xiaowang/PycharmProjects/psSite/template"

def getLog():
    return logging;