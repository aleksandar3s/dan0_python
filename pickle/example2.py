import pickle

if __name__ == "__main__":
    h = open("tocka.pkl", "rb")
    pk = pickle.load(h)
    h.close()
    print(pk)

    
