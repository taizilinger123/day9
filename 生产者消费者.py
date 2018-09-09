import  threading,time
import queue

q = queue.Queue(maxsize=10)

def Producer(name):
       count = 1
       while True:
            q.put("骨头%s" %count)
            print("生产了骨头",count)
            count += 1
            time.sleep(2)

def Consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name,q.get()))
        time.sleep(1)

p = threading.Thread(target=Producer,args=("盛磊",))
c = threading.Thread(target=Consumer,args=("陈超峰",))
c1 = threading.Thread(target=Consumer,args=("黄海华",))

p.start()
c.start()
c1.start()