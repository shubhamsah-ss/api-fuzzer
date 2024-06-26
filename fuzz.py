import requests
import sys


def loop(baseUrl):
    count = 0
    for line in sys.stdin:
        word = line.strip()
        res = requests.get(url=f"{baseUrl}/{word}")
        count += 1
        sys.stdout.write(f"\rWord count: {count}")
        sys.stdout.flush()
        if res.status_code == 404: 
            continue
        else:
            print("\n" + word + "\n")
            print(res)
            data = res.json()
            print(len(data))

baseUrl = sys.argv[1]

loop(baseUrl)
