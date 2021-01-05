# exerice 1
def ex1():
    cubes = [i**3 for i in range(4)]
    multiples = [i*0.02 for i in range(4)]
    return cubes, multiples

# exercice 2
def ex2():
    x = [(i+1)/10 for i in range(20)]
    y = [i**3 for i in x]
    z = [1/i for i in x]
    return x, y, z

# exercice 3
a = [2,1,0.5]
print(a)
a[1] = 2
print(a)
del a[2]
print(a)
a.append(3)
print(a)

print("\nPARIE 2!!!!\n")

a = [2,1,0.5]
print(a)
a = [3] + a
print(a)
a[1] = 2
print(a)
del a[2]
print(a)

# exercice 4
print("EXERCICE 4!!!!")
v = []
a = 1
v.append(a)
a = a*3
v.append(a)
a = a*2
v.append(a)
a = a*2
v.append(a)
a = a*3
v.append(a)
print(v)