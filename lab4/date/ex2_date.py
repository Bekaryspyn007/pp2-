# Write a Python program to print yesterday, today, tomorrow.

import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)

print("Yesterday: " + str(yesterday))
print("Today: " + str(today))
print("tomorrow: " + str(tomorrow))
