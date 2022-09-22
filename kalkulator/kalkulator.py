print("Kalkulator, ki naredi zeljen operacijo nad dve stevili")

while True:

    operacija = input("Vnesi zeljeno operacijo v obliki operaterja v narekovajih (npr. +,-,*,/ ...): ")
    stevilo1 = input("Vnesi prvo stevilo: ")
    stevilo2 = input("Vnesi drugo stevilo: ")

    if(operacija == '+'):
        print(int(stevilo1) + int(stevilo2))
    elif(operacija == '-'):
        print(int(stevilo1) - int(stevilo2))
    elif(operacija == '*'):
        print(int(stevilo1) * int(stevilo2))
    elif(operacija == '/'):
        print(int(stevilo1) / int(stevilo2))
    else:
        print("Napacen vnos, prosimo se enkrat preverite veljavnost operacije ali veljavnost stevilk")
    
    konec = input("Ali zelite novo racunanje(da/ne): ")
    if konec == "ne":
        print("Hvala za uporabo!")
        break
    
        



