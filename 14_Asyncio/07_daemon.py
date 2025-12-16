import threading 
import time


def monitor_tea_temp():
    print(f"Monitoring tea temperature...")
    time.sleep(2)
    
t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main Program done")

