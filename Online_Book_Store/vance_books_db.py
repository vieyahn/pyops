
#coding=utf-8
import os.path
import tornado.locale
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pymongo import MongoClient

from tornado.options import options,define
import pymongo

define("port",default=8000,help="run on the given port",type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "Vance's Books | Home",
            header_text = "Welcome to Vance's Books"
        )


class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        self.render(
            "recommended.html",
            page_title = "Vance's Books | Recommended Reading",
            header_text = "Recommended Reading",
            books = books
        )

class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string(
            "modules/book.html",
            book=book,
        )

    def css_files(self):
        return "/static/css/style.css"
    def javascript_files(self):
        return "static/js/script.js"


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",MainHandler),
            (r"/recommended/",RecommendedHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            ui_modules={"Book":BookModule},
            debug=True,
        )
        conn = MongoClient("localhost",27017)
        self.db = conn["bookstore"]
        tornado.web.Application.__init__(self,handlers,**settings)
        

        
if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()




