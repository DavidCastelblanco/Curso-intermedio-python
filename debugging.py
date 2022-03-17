def divisors(num):
   
    divisors =[]
    for i in range (1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors
   
    # divisors = [i for i in range(1,num+1) if num % i ==0]
    # return divisors




def run():
    try:
        num = int(input('ingresa un numero: '))
        if num<=0:
            raise ValueError ('No se pueden ingresar numeros negativos')        
    #     divisors = list(filter(lambda i: num % i ==0, range(1,num+1)))
        print(divisors(num))
        print('termino mi programa')

    except ValueError:
        print('Solo ingresar numeros enteros positivos, no letras o numeros negativos')


if __name__ == '__main__':
    run()