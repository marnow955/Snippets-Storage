# -*- coding: utf-8 -*-
from vial import Vial, render_template, not_found, serve_static
from regist import regist as regist_user
from login import login as login_user

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

def regist(headers, body, data):
  try:
    email = str(data['email'])
    password = str(data['password1'])
    if regist_user(email, password):
      data['message'] = "Welcome on Snippets Storage!"
      data['href'] = "/"
      data['hrefmess'] = "Sign In"
      return render_template('message.html', body=body, data=data), 200, {}
    else:
      data['message'] = "You already have an account."
      data['href'] = "/"
      data['hrefmess'] = "Sign In"
      return render_template('message.html', body=body, data=data), 200, {}
  except:
    return not_found(headers, body, data, headers['request-uri'], prefix)

def login(headers, body, data):
  try:
    if int(data['logged']==1) and data['userid']:
      return upload(headers, "logged", data)
  except:
    pass
  try:
    email = str(data['email'])
    password = str(data['password'])
    if login_user(email, password):
      return upload(headers, "if", data)
    else:
      data['message'] = "We could not log you, please, check your email and password"
      data['href'] = "/"
      data['hrefmess'] = "Try again"
      return render_template('message.html', body=body, data=data), 200, {}
  except:
    return not_found(headers, body, data, headers['request-uri'], prefix)

def main(headers, body, data):
  return render_template('main.html', body=body, data=data), 200, {}

def hello(headers, body, data, name):
  return 'Howdy ' + name, 200, {}

def upload(headers, body, data):
  return render_template('upload.html', body=body, data=data), 200, {}

routes = {
  '/': index,
  '/register': register,
  '/hello/{name}': hello,
  '/upload': upload,
  '/login': login,
  '/main': main,
  '/regist': regist,
}

app = Vial(routes, prefix=prefix, static='/static').wsgi_app()

