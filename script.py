import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who):
    greeting = "Hello, {}".format(who)
    # greeting = f'Hello, {who}' # for Python ver >= 3.6
    return greeting


print(greet("World"))
print(greet("Hugh"))

url = "https://coreyms.com"
print(f"Fetching {url}")
r = requests.get(url)
print(f"The status code is {r.status_code}")

name = input("Your name? ")
print(f"Hello {name}")