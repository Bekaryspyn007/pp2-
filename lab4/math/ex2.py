'''
Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5
'''

h = int(input('Height: '))
a = int(input('Base, first value: '))
b = int(input('Base, second value: '))

print('Expected Output: ' + str((a+b)*0.5*h))