# Write a Python program to calculate two date difference in seconds.

import datetime

a = datetime.datetime.now()
b = datetime.datetime.now().replace(hour=16)

print((a - b).total_seconds())