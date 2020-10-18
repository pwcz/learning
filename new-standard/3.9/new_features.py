#!/usr/bin/env python3.9
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, available_timezones

# based on https://realpython.com/python39-new-features/

print("Proper Time Zone Support\n"
      "Old way:\n")

print(f"Current time with UTC time zone aware: {datetime.now(tz=timezone.utc)}")
print(f"Naive timestamp, without time zone information: {datetime.now()}")

print("\nNew way:\n")

current_time = datetime.now(tz=ZoneInfo("Europe/Warsaw"))
print(f"Current local time: {current_time}")
london_time = current_time.astimezone(ZoneInfo("Europe/London"))
print(f"Current local time in London: {london_time}")

print(f"Currenly available timezones: {len(available_timezones())}")

tz = ZoneInfo("Europe/Warsaw")

print(f"Time in Warsaw: {current_time:%b %d, %Y at %H:%M} {tz.tzname(current_time)}")

# Simpler Updating of Dictionaries

pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

print({**pycon, **europython})

merged = pycon.copy()
for key, value in europython.items():
    merged[key] = value

print(merged)

(merged_2 := pycon.copy()).update(europython)
print(merged_2)

# new way

print(pycon | europython)
pycon |= europython
print(pycon)

# other types

libraries = {
    "collections": "Container datatypes",
    "math": "Mathematical functions",
}
libraries |= [("graphlib", "Functionality for graph-like structures")]
print(libraries)


