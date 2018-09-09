from multiprocessing import Process,Queue
import threading
#import queue

# def f(q):
#     q.put([42, None, 'hello'])

def f(qq):
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    #p = threading.Thread(target=f,)
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()