'''Multithreading in Python: Advanced Details
Multithreading is when your Python program runs multiple threads within the same process. A thread is like a lightweight sub-program that shares memory with the main program. It's great for tasks where you're waiting a lot, like downloading files or reading from networks, because one thread can wait while another works.
But here's the big catch in Python (CPython specifically): the **Global Interpreter Lock (GIL). The GIL is a lock that allows only one thread to run Python code at a time. Why? To make memory management safe and simple, especially for reference counting. This means:
- For I/O-bound tasks(waiting for input/output like web requests or file reads), multithreading works well because threads release the GIL during waiting, letting others run.
- For CPU-bound tasks(heavy calculations like math loops or image processing), multithreading doesn't speed things up much. Threads take turns holding the GIL, so it's like single-threaded on multi-core CPUs.

Advanced limitations of GIL:
- Even on a 16-core CPU, CPU-intensive threads won't use all cores — they're serialized (one at a time).
- GIL release happens on I/O or after a certain number of bytecode instructions (about every 5ms), but this adds overhead (context switching).
- In multi-threaded code, if one thread holds GIL too long (e.g., in a tight loop), others starve.
- Workarounds: Use multiprocessing (separate processes, no GIL shared), or libraries like Numba/JAX that release GIL, or switch to Jython/IronPython (no GIL, but less popular).
'''
import threading
import time
from multiprocessing import Process, Pool, Value
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# multithreading
def worker(num):
    print(f"worker {num} starting")
    time.sleep(2)
    print(f"worker {num} done")


def increment_thread(lock, counter):
    for _ in range(100000):
        with lock:
            counter[0] += 1


''' Multiprocessing in Python: Advanced Details
Multiprocessing runs multiple separate processes (not threads). Each process has its own Python interpreter and memory space, so **no GIL issue** — true parallelism on multi-core CPUs.
Great for CPU-bound tasks (math, simulations, data processing). But overhead: processes are heavier than threads (slower to start, more memory, communication needed via queues/pipes).
Key classes: Process (single process), Pool (group of workers for parallel tasks).
'''

'''Advanced tips:
- Shared memory: Use `Value` or `Array` for simple shared data (no GIL fights since separate processes).
- Queues/Pipes: For communication between processes.
- Chunksize: In Pool.map, set chunksize for large lists to reduce overhead.
- Limitations: Functions must be picklable (no lambdas, define at top level). Processes don't share memory easily — use Manager for shared dict/list (slower).
'''

def process_worker(num):
    print(f"process {num} starting")
    time.sleep(2)
    print(f"process {num} done")


def square(n):
    return n * n


def increment_process(shared_counter):
    for _ in range(100000):
        with shared_counter.get_lock():
            shared_counter.value += 1


def multiply_range(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def parallel_factorial(n, num_processes=4):
    if n <= 1:
        return 1

    chunk_size = n // num_processes
    chunks = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes)]
    chunks[-1] = (chunks[-1][0], n)

    with Pool(num_processes) as pool:
        results = pool.starmap(multiply_range, chunks)

    final = 1
    for r in results:
        final *= r
    return final


'''Web Scraping in Python: Advanced Techniques
Web scraping = getting data from websites using code. Basic: requests + BeautifulSoup. Advanced: Handle blocks, dynamic JS, pagination, concurrency.
Key libraries: requests (HTTP), BeautifulSoup (parse HTML), Selenium (for JS sites).

# Advanced tips:
- Headers & User-Agent: Pretend to be a browser to avoid blocks.
Proxies & Rotation: Use free/paid proxies to change IP.
- Pagination: Loop over pages.
- Dynamic/JS sites: Use Selenium to run browser.
- Rate limiting: Add time.sleep(2) between requests to avoid bans.
- AJAX/Forms: Use Selenium or inspect network for API URLs.
- Legal/Ethical: Check robots.txt, don't overload servers, respect terms.

'''


def simple_scrape():
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get("https://example.com", headers=headers, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    print("H1:", soup.find('h1').text)


def selenium_scrape():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://example.com")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print("Title:", soup.title.text)
    driver.quit()



# MAIN EXECUTION BLOCK

if __name__ == "__main__":

    # ----- THREADING -----
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("all workers finished")

    # Thread with lock
    counter = [0]
    lock = threading.Lock()

    threads = [threading.Thread(target=increment_thread, args=(lock, counter)) for _ in range(10)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("thread counter:", counter[0])


    # ----- MULTIPROCESSING -----
    processes = []
    for i in range(5):
        p = Process(target=process_worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("all processes finished")


    # Pool example
    numbers = [1,2,3,4,5,6,7,8,9,10]
    with Pool(4) as pool:
        results = pool.map(square, numbers)

    print("squares:", results)


    # Shared Value example
    counter = Value('i', 0)
    processes = [Process(target=increment_process, args=(counter,)) for _ in range(10)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("process counter:", counter.value)


    # Factorial
    print("factorial(10):", parallel_factorial(10))


    # Web Scraping (optional)
    simple_scrape()
    # selenium_scrape()  # uncomment if chromedriver setup ready

''' Multiprocessing in Python: Advanced Details
Multiprocessing runs multiple separate processes (not threads). Each process has its own Python interpreter and memory space, so **no GIL issue** — true parallelism on multi-core CPUs.
Great for CPU-bound tasks (math, simulations, data processing). But overhead: processes are heavier than threads (slower to start, more memory, communication needed via queues/pipes).
Key classes: Process (single process), Pool (group of workers for parallel tasks).
'''

'''Advanced tips:
- Shared memory: Use `Value` or `Array` for simple shared data (no GIL fights since separate processes).
- Queues/Pipes: For communication between processes.
- Chunksize: In Pool.map, set chunksize for large lists to reduce overhead.
- Limitations: Functions must be picklable (no lambdas, define at top level). Processes don't share memory easily — use Manager for shared dict/list (slower).
'''


