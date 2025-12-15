import threading
import requests
import time


def download(url):
    print(f"Staring download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")
    
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
end = time.time()

print(f"All downloads done in {end - start:.2} seconds")


