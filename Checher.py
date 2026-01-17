import requests
import time

def check_endpoints():
    endpoints = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/users"
    ]
    
    print(f"{'URL':<50} | {'Status':<7} | {'Time (s)':<10}")
    print("-" * 75)

    for url in endpoints:
        start_time = time.time()
        try:
            response = requests.get(url, timeout=5)
            latency = round(time.time() - start_time, 3)
            status = response.status_code
            print(f"{url:<50} | {status:<7} | {latency:<10}")
        except Exception as e:
            print(f"{url:<50} | Error   | {e}")

if __name__ == "__main__":
    check_endpoints()
