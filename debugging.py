# CODE ERROR
# def divisor(num):
#     divisors = [i for i in range(1,num+1) if num % i ==1]
#     return divisors



# def run():
#     num=int(input("ingresa un numero:"))
#     print(divisor(num))
#     print("termino el programa")


# if __name__ == '__main__':
#     run()


#break point 
def divisor(num):
    divisors = [i for i in range(1,num+1) if num % i ==0]
    return divisors



def run():
    try:
        num=int(input("ingresa un numero:"))
        print(divisor(num))
        print("termino el programa")
    except ValueError:
        print("Debes igresar un numero")

if __name__ == '__main__':
    run()