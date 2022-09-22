import copy



def vhodnaF():
    '''test = 1
    l1 = [1, True, "Bostjan", 0.004, test, [1, 0.4]]
    print(l1[2])

    d1 = {"ABC": 123, 17:"Nekaj"}
    print(d1["ABC"])
    

    t1 = (1, 7, 4,)

    l1[1] = False
    print(l1)

    l1.append(1111)
    print(l1)

    l1.pop()
    print(l1)

    l1.insert(3, "asd")
    l1.remove(1)

    d1["asd"] = 12345

    print(l1.index("asd")) #isce na kateri index se nahaja ta vrednost '''

    l1 = [1, 2, 3, 4]

    l2 = copy.deepcopy(l1)

    l2.append(7)
    print(l1)
    print(l2)



if __name__ == "__main__": #__name__ je parameter skripte
    vhodnaF()

