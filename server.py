#encoding=utf-8
import sys
sys.path.append("F:\web\UIModules")
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path
import secure_password
import connection
from UIModules import equipmentSelectorUIModule
from UIModules import componentSelectorUIModule

from tornado.options import define, options
define("port", default=8080, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("userName")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", indexHandler),
            (r"/admin", adminIndexHandler),
            (r"/login", loginHandler),
            (r"/logout", logoutHandler),
            (r"/getCpSelector/(\w+)", getCpSelectorHandler),
        ]
        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "cookie_secret": "2aTn2WgKR/+SFyXK79MmFx4uTxwZh0jTlRGUHuhy7YI=",
            "xsrf_cookies": True,
            "login_url": "/login",
            "debug": True,
            "ui_modules": {
                "equipmentSelector": equipmentSelectorUIModule,
                "componentSelector": componentSelectorUIModule,
            }
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class loginHandler(BaseHandler):
    def get(self):
        self.render(
            "login.html",
            page_title = "用户登录",
            switch_title = "管理员入口",
            switch_link = "admin",
        )
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        db = connection.connection()
        conn = db.connect()
        cur = conn.cursor()
        cur.execute('select password from user where userName=%s', username) 
        rs = cur.fetchall()
        if secure_password.validate_password(rs[0][0], password):
            self.set_secure_cookie('userName',username)
        else:
            pass
        conn.commit()
        cur.close()
        conn.close()
        self.redirect("/")

class logoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("userName")
        self.redirect("/")

class indexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render(
            "index.html",
            page_title = "首页",
            username = self.current_user,
        )

class getCpSelectorHandler(BaseHandler):
    def get(self, eqID):
        self.render("cpSelector.html", eqID = eqID)

class adminIndexHandler(BaseHandler):
    def get(self):
        self.render(
            "admin-login.html",
            page_title = "管理员登陆",
            switch_title = "普通用户入口",
            switch_link = "",
        )

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()