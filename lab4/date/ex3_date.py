# Write a Python program to drop microseconds from datetime.

import datetime

v = datetime.datetime.now()

def drop(v):
    ds = v.replace(microsecond=0)
    return ds
    
print(drop(v))