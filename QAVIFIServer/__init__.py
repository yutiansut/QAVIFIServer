
import tornado
from tornado.web import Application, RequestHandler, authenticated
from tornado.websocket import WebSocketHandler
from qavifiserver.qahqchart import QAHqchartDailyHandler, QAHqchartKlineHandler

__version__ = '0.0.2'
__author__ = 'yutiansut'

def run_server():

    app=Application(
        handlers=[
            (r"/test",  QAHqchartDailyHandler),
            (r"/testk", QAHqchartKlineHandler)
        ],
        debug=True
    )
    app.listen(8029)
    tornado.ioloop.IOLoop.current().start()
