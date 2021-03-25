list1 = [10,20,30]
list2 = ["luc","leny","lalie"]
list3 = [[11,5,21],[1],[2,13]]

print("list1[0]      = "+str(list1[0]))
print("list3[-1]     = "+str(list3[-1]))
print("list3[0]      = "+str(list3[0]))
print("list3[0][-1]  = "+str(list3[0][-1]))
print("list3[0][1]   = "+str(list3[0][1]))
print("list3[-1][-1] = "+str(list3[-1][-1]))

print()

liste = [i for i in range(20)]
print("liste ------------> "+str(liste))
print("liste[4 :10 :2] --> "+str(liste[4 :10 :2]))

def f(x):
    return 2*x**2+x/2-4
list = [i/4 for i in range(5)]
images = [f(i) for i in list]
print(list, images)