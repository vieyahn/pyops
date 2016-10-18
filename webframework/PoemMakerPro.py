# coding=utf-8
import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
#HTML表单

from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class PoemPageHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        noun1 = self.get_argument('noun1')#从get方法中获取这些参数
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html',roads = noun1,wood = noun2,made = verb,difference = noun3) #render方法 让浏览器传送HTML
                                                                # 同时render方法会在本地目录的templates文件夹中查找html文件

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/',IndexHandler),(r'/poem',PoemPageHandler)],
        template_path = os.path.join(os.path.dirname(__file__),"templates")

    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
