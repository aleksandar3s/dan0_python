





class Pravokotnik(object):
    barva = "rdeca" #vsi pravokotniki na tak nacini ibojo imeli enako barvo
    def __init__(self, a, b):
        print("sem nov pravokotnik")
        self.a = a
        self.b = b

        pass

    def ploscina(self):
        return self.a * self.b 

    def obseg(self):
        return 2*self.a * 2*self.b


    def __del__(self):
        print("brisem pravokotnik")


class Kvadrat(Pravokotnik):  #inheritance
    def __init__(self, a):
        super(Kvadrat, self).__init__(a,a)
        

print(__name__)
if __name__ == "__main__":

    prav1 = Pravokotnik(5.0, 4.0)
    print(prav1.ploscina())
    print(prav1.obseg())
    kv1 = Kvadrat(4.0)
    print(kv1.ploscina())
