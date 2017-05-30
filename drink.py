# -*- coding: utf-8 -*-
from vial import Vial, render_template

def index(headers, body, data):
  return 'Hello', 200, {}

def hello(headers, body, data, name):
  return 'Howdy ' + name, 200, {}

bodyr = "<h1>marek</h1>"
def upload(headers, body, data):
  return render_template('upload.html', body=bodyr, data=data), 200, {}

routes = {
  '/': index,
  '/hello/{name}': hello,
  '/upload': upload,
}

app = Vial(routes, prefix='/bach/drink', static='/static').wsgi_app()
