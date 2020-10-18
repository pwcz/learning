#!/usr/bin/env python3.9
from typing import Annotated
from typing import get_type_hints

# def speed(distance: "feet", time: "seconds") -> "miles per hour":
#     """Calculate speed as distance over time"""
#     fps2mph = 3600 / 5280  # Feet per second to miles per hour
#     return distance / time * fps2mph


# def speed(distance: Annotated[float, "feet"], time: Annotated[float, "seconds"]) -> Annotated[float, "miles per hour"]:
#     """Calculate speed as distance over time"""
#     fps2mph = 3600 / 5280  # Feet per second to miles per hour
#     return distance / time * fps2mph


# Feet = Annotated[float, "feet"]
# Seconds = Annotated[float, "seconds"]
# MilesPerHour = Annotated[float, "miles per hour"]
#
#
# def speed(distance: Feet, time: Seconds) -> MilesPerHour:
#     """Calculate speed as distance over time"""
#     fps2mph = 3600 / 5280  # Feet per second to miles per hour
#     return distance / time * fps2mph

class AnnotationFactory:
    def __init__(self, type_hint):
        self.type_hint = type_hint

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return Annotated[(self.type_hint, ) + key]
        else:
            return Annotated[self.type_hint, key]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type_hint})"


Float = AnnotationFactory(float)
print(Float)


def speed(distance: Float["feet"], time: Float["seconds"]) -> Float["miles per hour"]:
    """Calculate speed as distance over time"""
    fps2mph = 3600 / 5280  # Feet per second to miles per hour
    return distance / time * fps2mph


print(speed.__annotations__)
print(speed.__annotations__["distance"].__metadata__)
print(get_type_hints(speed))
