from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import Application, FallbackHandler, StaticFileHandler
from extensions import base
from flask import Flask
from nameko.runners import ServiceRunner
from regular_jobs import RegularJobs
import threading


def app_factory(name=None):
    app = Flask(name or __name__)
    app.register_blueprint(base.app)

    return app


if __name__ == '__main__':
    app = app_factory()
    app.debug = True

    wsgi_container = WSGIContainer(app)

    tornado_app = Application(
        [
            # (r"/statics/(.*)", StaticFileHandler, dict(path=app_path + "/statics/")),
            ('.*', FallbackHandler, dict(fallback=wsgi_container)),
        ])
    http_server = HTTPServer(tornado_app)
    http_server.listen(8080)

    def regular_job_runner():
        print('fdf')
        runner = ServiceRunner(config={})
        runner.add_service(RegularJobs)
        runner.start()
        runner.wait()
    regular_job_thread = threading.Thread(target=regular_job_runner)
    regular_job_thread.start()

    IOLoop.instance().start()
