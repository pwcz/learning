#!/usr/bin/env python3.8


def incr(x):
    return x + 1


print(incr(1))
print(incr(1.2))
print(incr(x=2))


def incr(x, /):
    return x + 1


incr(3.8)

try:
    incr(x=3.8)
except TypeError:
    print("Exception on call")


def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"


print(greet("Johny"))
print(greet("Johny", greeting="Awesome job"))
try:
    greet(name="Johny", greeting="Awesome job")
except TypeError:
    print("Exception on call")


def to_fahrenheit(*, celsius):
    return 32 + celsius * 9 / 5


try:
    to_fahrenheit(36)
except TypeError:
    print("Exception on call")
print(to_fahrenheit(celsius=38))


def headline(text, /, border="♦", *, width=50):
    return f" {text} ".center(width, border)


print(headline("Positional-only Arguments"))


print(headline("Python 3.8", "="))
print(headline("Real Python", border=":"))
print(headline("Python", "🐍", width=28))

try:
    print(headline("Python", "🐍", 38))
except TypeError:
    print("Exception on call")
