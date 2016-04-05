A very basic web application using the
[CherryPy](http://cherrypy.org/) framework and Python 3.5.

The image is quite light thanks to
[Alpine Linux](https://hub.docker.com/r/frolvlad/alpine-python3/).


Run it
======

Run it as follows:

$ docker run --name cherrypy -d -p 8080:8080 lawouach/cherrypy-hello-world

You can point your browser to http://locahost:8080/

You can view the logs like this:

$ docker logs cherrypy

Finally you can stop the server as follows:

$ docker stop cherrypy


Build it
========

You may rebuild the image:

$ docker build -t <MYREPO>/<IMAGE_NAME> .
