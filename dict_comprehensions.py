from math import sqrt
def run():
    # dicc = {}

    # # for i in range(1,101):
    # #     if i%3 !=0:
    # #         dicc[i] = i**3

    # dicc_com = {i: i**3 for i in range (1,101) if i%3 !=0}

    # print(dicc_com)

    my_dict2 = {i: round(sqrt(i),2) for i in range (1, 100)}

    print(my_dict2)


if __name__ == '__main__':
    run()
