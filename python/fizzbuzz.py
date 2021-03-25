# -*- coding: utf-8 -*-

n = 1

while n <= 100:
    if n%3 == 0 and n%5 == 0:
        print("FIZZBUZZ ("+str(n)+")")
    elif n%3 == 0:
        print ("fizz ("+str(n)+")")
    elif n%5 == 0:
        print("buzz ("+str(n)+")")
    else:
        print(n)
        
    n += 1
