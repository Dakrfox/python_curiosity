def divisor(num):
    divisors = [i for i in range(1,num+1) if num % i ==0]
    return divisors



def run():
    num=input("ingresa un numero:")
    assert num.isnumeric() and int(num)>0, "no es un entero positivo"
    print(divisor(int(num)))
    print("termino el programa")
    

if __name__ == '__main__':
    run()