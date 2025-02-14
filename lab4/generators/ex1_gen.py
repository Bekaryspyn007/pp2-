# Create a generator that generates the squares of numbers up to some number N.

def gen(squareNum):
    for i in range(squareNum):
        sq = i*i
        yield sq
        
print(list(gen(10)))
        