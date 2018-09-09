from greenlet import greenlet #安装gevent包
#pycharm安装包file-settings-Project:Pycharm-Project Interpreter-点+在搜索框里直接输入要安装的包名(gevent)-下面的方框打钩
#-直接点击Install Package就好了

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1) #启动一个携程
gr2 = greenlet(test2)
gr1.switch()