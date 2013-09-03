# -*-coding:utf-8-*-
__author__ = 'wanghongmeng'

from db import datasource
from model import modelType

pool = datasource.initDBPool()

def getSitePerson():
    try:
        sitePersons = datasource.query(pool,"select id,person_name,person_photo,person_comment from site_person order by person_idx")
        personList = []
        for sitePerson in sitePersons:
            id = sitePerson[0]
            personName = sitePerson[1]
            personPhoto = sitePerson[2]
            personComment = sitePerson[3]
            person = modelType.SitePerson(id,personName,personPhoto,personComment)
            personList.append(person)
        return personList
    except Exception, e:
        print e

def getCatagoryName():
    catagoryNames = datasource.query(pool,"select * from catagory_name")
    return catagoryNames