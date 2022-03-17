def divisors(num):
    assert num !=0, 'El número no debe ser 0'
   
    divisors =[]
    for i in range (1,num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors
   
   
def run():
    num = input('ingresa un numero: ')
    assert num.isnumeric(), 'Debes ingresar un número'

    print(divisors(int(num)))
    print('termino mi programa')

    
if __name__ == '__main__':
    run()