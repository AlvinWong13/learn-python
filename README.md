-- hello world
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

-- Strings and arrays in python
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Hello")
strings.append('World!')

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

-- name and age
name = "Alvin"
age = 29
print("%s is %d years old." % (name, age))

-- string format with data
data = ("Alvin", "Wong", 100.54)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

-- fizzbuzz

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