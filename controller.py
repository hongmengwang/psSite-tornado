#coding=UTF-8
__author__ = 'wanghongmeng'


import tornado.ioloop
import tornado.web
import tornado.httputil
import config
from service import frontService

class Index(tornado.web.RequestHandler):
    def get(self):
        try:
            personList = frontService.getSitePerson()
            loader = tornado.web.template.Loader(config.template_path)
            self.write(loader.load("index.html").generate(personList = personList))
        except Exception,e:
            print e

application = tornado.web.Application([
    (r"/", Index)
])

if __name__ == "__main__":
    application.listen(9090)
    tornado.ioloop.IOLoop.instance().start()