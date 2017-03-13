import cherrypy


class Logger(object):
    """Classe Logger"""

    @cherrypy.expose()
    def log(self):
        return "phrase loggée"

if __name__ == '__main__':
    cherrypy.quickstart(Logger(), '/')
