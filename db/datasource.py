#coding=UTF-8
__author__ = 'wanghongmeng'

import MySQLdb
from DBUtils.PooledDB import PooledDB

database_maxcached = 5
database_maxshared = 5
database_maxconn = 10
database_host = "127.0.0.1"
database_username = "root"
database_password = "admin"
database_port = 3306
database_schema = "pssite_db"
databse_charset = "utf8"

def initDBPool():
    return PooledDB(MySQLdb,maxcached=database_maxcached,maxshared=database_maxshared,maxconnections=database_maxconn,user=database_username,passwd=database_password,host=database_host,port=database_port,db=database_schema,charset=databse_charset)

def query(pool, sql, params={}):
    if pool is None or sql is None:
        return []

    try:
        conn = pool.connection()
        cursor = conn.cursor()

        #执行查询 语句
        cursor.execute(sql, params);

        #查询所有记录
        res = cursor.fetchall()

        return res
    except Exception,e:
        print e.message
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass

def update(pool, sql, params={}):
    if pool is None or sql is None:
        return []

    try:
        conn = pool.connection()
        cursor = conn.cursor()

        #执行语句

        cursor.execute(sql,params)

        conn.commit()


    except Exception,e:
        print e
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass