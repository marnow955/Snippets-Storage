# -*- coding: utf-8 -*-
from vial import Vial, render_template, not_found

prefix = "Snippets-Storage"

def index(headers, body, data):
  #if data['username'] != 'admin' or data['password'] != 'admin':
  #  return render_template('index.html'), 200, {}
  #else:
  #  return redirect(url_for('upload'))

  return render_template('index.html'), 200, {}
  #return 'Hello', 200, {}

def register(headers, body, data):
  return render_template('register.html'), 200, {}

def login(headers, body, data):
  try:
    username = str(data['username'])
    password = str(data['password'])
    if username == 'admin' and password == 'admin123':
      return upload(headers, "if", data)
    else:
      return upload(headers, "else", data)
  except:
    return not_found(headers, body, data, headers['request-uri'], prefix)

def main(headers, body, data):
  return render_template('main.html', body=body, data=data), 200, {}

def hello(headers, body, data, name):
  return 'Howdy ' + name, 200, {}

bodyr = "<h1>marek</h1>"
def upload(headers, body, data):
  return render_template('upload.html', body=body, data=data), 200, {}

routes = {
  '/': index,
  '/register': register,
  '/hello/{name}': hello,
  '/upload': upload,
  '/login': login,
  '/main': main,
}

app = Vial(routes, prefix=prefix, static='/static').wsgi_app()

