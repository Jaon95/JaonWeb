import threading
mydata = threading.local()
mydata.number = 42
log = []

print(mydata.number)

def f():
    mydata.number = 11
    log.append(mydata.number)

thread = threading.Thread(target=f)
thread.start()
thread.join()
print(mydata.number)
print(log)