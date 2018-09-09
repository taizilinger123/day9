from wsgiref.simple_server import make_server

def f1(request):
    return  [b'<h1>Hello, book!</h1>']
def f2(request):
    return  [b'<h1>Hello, web!</h1>']
def login(request):
    print(request)
    return [b'<h1>Hello, loggin!</h1>']

def routers():
    urlpatterns = (
        ('/book',f1),
        ('/web',f2),
        ('/login',login),
    )
    return urlpatterns

def application(environ, start_response):
    #print("environ",environ)
    #print("environ",environ["PATH_INFO"])
    start_response('200 OK', [('Content-Type', 'text/html')])
    path=environ["PATH_INFO"]

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func(environ)
    else:
        return ["<h1>404</h1>".encode("utf8")]

    # if path=="/book":
    #     return f1(environ)
    # elif path=="/web":
    #     return f2(environ)
    # else:
    #     return ["<h1>404</h1>".encode("utf8")]

#1.封装socket对象以及准备过程(socket,bind,listen)
httpd = make_server('', 8080, application)
# ctrl+b跳转到类的实现

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
# ctrl+b跳转到类的实现
#运行不显示就启动任务管理器---进程---python.exe结束进程就可以看到输出效果了.