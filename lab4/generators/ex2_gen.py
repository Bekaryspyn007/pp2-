# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console

def gene(n):
    for i in range(0,n,2):
        yield i
        
print(list(gene(18)))