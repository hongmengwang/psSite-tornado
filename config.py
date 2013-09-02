__author__ = 'hongmengwang'

import logging
import time
import MySQLdb

logfile = "/home/wanghongmeng/psSite/logs/" + time.strftime("%Y%m%d") + ".log"
logging.basicConfig(level = logging.DEBUG,format="[%(asctime)s]:[%(name)s]:[%(levelname)s]:[%(pathname)s]:[line-number:%(lineno)d]:[%(message)s]",datefmt="%Y-%m-%d %H:%M",filename = logfile)


def getLog():
    return logging;