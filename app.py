import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return "Hello world!"

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Root())
