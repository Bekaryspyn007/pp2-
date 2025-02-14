# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.


def gen3and4(v):
    for i in range(v):
        if i%4 == 0 and i%3 == 0:
            yield i

print(list(gen3and4(30)))

        