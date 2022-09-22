import time 
#from time import sleep
#import time as t

a = 54
b = 82
print('Sestevek je ' + str(a+b))

''''
lahko je vecvrsticni komentar
'''


if a>b:
    print("a je vecji od b")
elif a<b:
    print("b je vecji od a")
else:
    print("noben pogoj ni izpolnjen")

while True:
    a += 1
    print("a je " + str(a))
    time.sleep(0.1)
    if a > b:
        break


vhod = input("Vnesi najljubso stevilo: ")
print("vasa stevilka je: "+ str(vhod))
