import threading, time


class ThreadDemo(threading.Thread):
    def run(self):
        print(f"{self.name} running")
        for i in range(3):
            print(f"Iteration {i+1}")
            time.sleep(1)
        print(f"{self.name} terminated")


thread1 = ThreadDemo()
print("Thread created")
time.sleep(1)
thread1.start()
print("Thread started")
thread1.join()
print("Execution complete")
# Output
# Thread created
# Thread-1 running
# Iteration 1
# Thread started
# Iteration 2
# Iteration 3
# Thread-1 terminated
# Execution complete
