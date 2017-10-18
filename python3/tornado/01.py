import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    # 主页请求方法
    def get(self):
        self.write("hello")
if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()
