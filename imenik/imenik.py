

def main():
    imenik = {"Ana":123456789, "Manca":789456123, "Mojca":1569753468, "Anastasija":159852456, "Aleksandar":963852741, "Boris":159753852} 

    '''for k,v in imenik.items():
        k_to_list = list(k)
        if(k.find("o", "i", "r")):
            print("Klicem " +  str(k) + " : " + str(v) )
    '''
    



    for k,v in imenik.items():
        k_to_list = list(k)
        if(k[0] == "A"):
            print("Klicem " + str(k) + " : " + str(v) )
    
    pass


if __name__ == "__main__":
    main()
