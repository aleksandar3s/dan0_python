

import time



def main():
    l1 = [1,3,3,5,6,6,3]
    
    for i in l1:
        print(i)

    l2 = [vred for vred in l1 if vred > 5]
    print(l2)

    d1 = {1:"a", 2:"b", 3:"c", 4:"d"}

    for _, v in d1.items(): # lahko damo tudi k,v ce rabimo tudi kljuce, ko damo podcrtaj pomeni da v tem primeru ne rabimo kljuce
        print(v)



    try: 
        d0 = 1/1
    except Exception as e:
        print("ni ratalo - " + str(e))

    finally:
        print("zakljuceno")




    try: 
        while True:
            print("neki")
            time.sleep(1)
    except KeyboardInterrupt as e:
        print("exiting - " )

    pass

if __name__ == "__main__":
    main()
