import threading

chai_stock = 0
lock = threading.Lock()

def restock():
    global chai_stock
    for _ in range(100000):
        with lock:
            chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(chai_stock)
