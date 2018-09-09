import multiprocessing
import time,threading

def thread_run():
    print(threading.get_ident())
def run(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_run,)
    t.start()

print(__name__)
if __name__ == '__main__':   #手动执行此脚本下面的脚本会被执行，如果作为模块被导入，下面的脚本不会被执行
    for i in range(10):
        p = multiprocessing.Process(target=run, args=('bob %s' %i,))
        p.start()
    #p.join()