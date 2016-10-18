import os

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from tornado.options import options,define
define('port',default=9000,type=int)


class ControlTem(tornado.web.RequestHandler):

    def get(self):
        bookss = ['vance', 'ariel', 'theo']
        self.render('control.html',books=bookss,title='Tornado',header='Python')




if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/',ControlTem)],
        template_path = os.path.join(os.path.dirname(__file__),"templates")

    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()