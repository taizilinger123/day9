import time
def current_time(request):
    product_list=models.product.object.all()
    cur_time = time.ctime(time.time())
    f=open("current_time.html","rb")
    data=f.read()
    data=str(data,"utf8").replace("!product_list!",product_list)
    return [data.encode("utf8")]

def f1():
    pass

def f2():
    pass

def f3():
    pass