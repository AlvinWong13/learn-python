import sys

import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('World!'))
print(greet('Alvin'))

data = ("Alvin", "Wong", 100.54)
format_string = "Hello %s %s. Your current balance is $%s."

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

r = requests.get("https://www.facebook.com")
print(r.status_code)
