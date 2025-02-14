# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

a = int(input())
b = int(input())


def gene(a,b):
    for i in range(a,b):
        yield i*i

for i in range(a,b):
    print(i*i ,end = ",")

print()

print(list(gene(a,b)))