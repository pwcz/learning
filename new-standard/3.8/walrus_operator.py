#!/usr/bin/env python3.8

print(walrus := True)

inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)

print(inputs)
