多线程:
import threading,queue
import time
from urllib import request
lock = threading.Lock()
url="https://www.taobao.com"
dataQueue = queue.Queue(maxsize=5)

def demand(num):
    while True:
        try:
            data=dataQueue.get(block=False)
        except queue.Empty:
             break
        with lock:
              r=request.urlopen(url)
              print(r.code)
        time.sleep(0.1)
        dataQueue.task_done()

if __name__ == "__main__":
    getThreads=[]
    for i in range (100):
        t=threading.Thread(target=demand,args=(i,))
        getThreads.append(t)
        t.start()

dataQueue.join()


多进程:
from multiprocessing import Pool,Process,Lock
from urllib import request

def clt_msg(num):
    url="https://www.taobao.com"
    r=request.get(url)
    print (r.code)

if __name__ == "__main__":
    pool=Pool(processes=5)
for i in range(100):
    pool.apply_async(clt_msg(i,))
    pool.close()
    pool.join()

#思考题:
#post与get区别：
#1.接的参数范围
#2.数据处理方式
#3.安全局限性

#post  常有四种  具体多少不知道









