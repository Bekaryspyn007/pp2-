"""
Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""

import math

n = int(input('Input number of sides: '))
a = int(input('Input the length of a side: '))

print('The area of the polygon is: ' + str(math.floor((n*a*a)/(4*math.tan((2*math.pi)/(2*n))))))