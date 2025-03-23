d = {0: 'a', 1: 'b', 2: 'c'}
for x in d.values():
 print(x)

 a="hello"
b=list(x.upper() for x in a)
print(b)

import random
print (random.choice([10.4, 56.99, 76]))

d = {"john":40, "peter":45}
print(list(d.keys()))

total = {}
def insert(item):
 if item in total:
    total[item] += 1
 else:
    total[item] = 1
insert('Apple')
insert('Ball')
insert('Apple')
print(len(total))