import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"{self.name} started")
        time.sleep(2)
        print(f"{self.name} finished")

# Creating threads
t1 = MyThread("Thread-1")
t2 = MyThread("Thread-2")

t1.start()
t2.start()

# Checking if threads are alive
print(f"Is {t1.name} alive?", t1.is_alive())
print(f"Is {t2.name} alive?", t2.is_alive())

# Joining threads to wait for their completion
t1.join()
t2.join()

print("All threads completed execution.")