import threading
import logging
import os

from flask import Flask
from nameko.runners import ServiceRunner
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import Application, FallbackHandler, StaticFileHandler

from util import slack
from api import base
from regular_jobs import RegularJobs


# class SlackLogHandle(logging.StreamHandler):
#     def emit(self, record):
#         slack.log("[%s]" % record.levelname + record.msg % record.args)


def app_factory(name=None):
    app = Flask(name or __name__)
    app.register_blueprint(base.app)

    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='LINE %(lineno)-4d  %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('LINE %(lineno)-4d : %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # if not os.environ.get('DEV', None):
    #     slack_log = SlackLogHandle()
    #     slack_log.setLevel(logging.INFO)
    #     logging.getLogger('').addHandler(slack_log)

    logging.info('Ready to start...')

    app = app_factory()
    app.debug = True

    wsgi_container = WSGIContainer(app)

    tornado_app = Application(
        [
            ('/', FallbackHandler, dict(fallback=wsgi_container)),
            ('/api/(.*)', FallbackHandler, dict(fallback=wsgi_container)),
            ("/(.*)", StaticFileHandler, dict(path=os.path.dirname(os.path.realpath(__file__)) + "/public/"))
        ])
    http_server = HTTPServer(tornado_app)
    http_server.listen(8080)

    def regular_job_runner():
        runner = ServiceRunner(config={})
        runner.add_service(RegularJobs)
        runner.start()
        runner.wait()
    regular_job_thread = threading.Thread(target=regular_job_runner)
    regular_job_thread.start()

    IOLoop.instance().start()
