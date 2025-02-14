# Implement a generator that returns all numbers from (n) down to 0.

def gene(n):
    for i in range(n,0,-1):
        yield i
        
print(', '.join(str(item) for item in list(gene(30))))