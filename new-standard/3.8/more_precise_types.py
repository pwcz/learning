#!/usr/bin/env python3.8
from typing import Literal
from typing import Union
from typing import overload
from typing import Final


def double(number: float) -> float:
    return 2 * number


double(3.14)
double("I'm not a float")


def draw_line(direction: Literal["horizontal", "vertical"]) -> None:
    if direction == "horizontal":
        ...  # Draw horizontal line

    elif direction == "vertical":
        ...  # Draw vertical line

    else:
        raise ValueError(f"invalid direction {direction!r}")


try:
    draw_line("up")
except ValueError:
    print("exception")


ARABIC_TO_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                   (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def _convert_to_roman_numeral(number: int) -> str:
    """Convert number to a roman numeral string"""
    result = list()
    for arabic, roman in ARABIC_TO_ROMAN:
        count, number = divmod(number, arabic)
        result.append(roman * count)
    return "".join(result)


@overload
def add(num_1: int, num_2: int, to_roman: Literal[True]) -> str: ...
@overload
def add(num_1: int, num_2: int, to_roman: Literal[False]) -> int: ...


def add(num_1: int, num_2: int, to_roman: bool = True) -> Union[str, int]:
    """Add two numbers"""
    result = num_1 + num_2

    if to_roman:
        return _convert_to_roman_numeral(result)
    else:
        return result


def test(input: int) -> None:
    print(f"test({input})")


test(add(10, 10, False))
print(add(5, 20, False))

ID: Final = 100
ID += 1  # only mypy warning
print(f"ID = {ID}")
