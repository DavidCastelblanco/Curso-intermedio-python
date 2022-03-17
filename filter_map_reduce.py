from functools import reduce
def run():

    my_list = [1,4,5,6,9,13,19,21]

    # odd = [i for i in my_list if i%2 !=0]

    #Aplicando filter
    odd = list(filter(lambda x: x%2 !=0, my_list))

    print(odd)

    #------------------------

    
    my_list2 = [1,2,3,4,5]

    # square = [i**2 for i in my_list2]

    #haciendolo con map

    square = list(map(lambda x: x**2, my_list2))

    print(square)

    #-------------------------

    my_list3 = [2,2,2,2,2]
    # resultado = 1
    # for i in my_list3:
    #     resultado *= i

    # Haciendolo con reduce
    resultado = reduce(lambda a,b: a*b, my_list3)


    print(resultado)

if __name__ == '__main__':
    run()