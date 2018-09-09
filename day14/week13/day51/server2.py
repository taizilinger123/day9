from wsgiref.simple_server import make_server

def application(environ, start_response):
    #2.通过environ封装成一个所有请求信息的对象
    #3.start_response可以很方便地设置响应头
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

#1.封装socket对象以及准备过程(socket,bind,listen)
httpd = make_server('', 8080, application)
# ctrl+b跳转到类的实现

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
# ctrl+b跳转到类的实现