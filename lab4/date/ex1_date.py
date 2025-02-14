# Write a Python program to subtract five days from current date.

import datetime

x = datetime.datetime.now()
v = x - datetime.timedelta(5)

print(x)
print(v)