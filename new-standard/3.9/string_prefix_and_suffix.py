#!/usr/bin/env python3.9

print("three cool features in Python".strip(" Python"))  # returns 'ree cool features i'


def remove_suffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    else:
        return text


print(remove_suffix("three cool features in Python", suffix=" Python"))
print(f"""empty suffix: {remove_suffix("three cool features in Python", suffix="")}""")

print("three cool features in Python".removesuffix(" Python"))
print("three cool features in Python".removeprefix("three "))
print("three cool features in Python".removeprefix("Something else"))
print(f""""Remove with empty prefix {"three cool features in Python".removeprefix("")}""")


# remove multiple occurrence

text = "Waikiki"
print(text.removesuffix("ki"))

while text.endswith("ki"):
    text = text.removesuffix("ki")

print(text)


