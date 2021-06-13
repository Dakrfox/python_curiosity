def read():
    numbers=[]
    with open("./files/numbers.txt","r" , encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    #con sobreescritura
    names=["facundo", "nicolás", "alejandro", "reginaldo", "victor"]
    with open("./files/names.txt", "w", encoding="utf-8")as f:
        for name in names:
            f.write(name)
            f.write("\n")
    #sin sobreescritura
    names2=["facundo", "nicolás", "alejandro", "reginaldo", "victor"]
    with open("./files/names2.txt", "a", encoding="utf-8")as f:
        for name in names2:
            f.write(name)
            f.write("\n")


def run():
    
    write()


if __name__ == '__main__':
    run()