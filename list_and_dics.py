def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {
        'fisrtname': 'David',
        'lastname': 'Castelblanco'
        }

    super_list = [
        {'fisrtname': 'David','lastname': 'Castelblanco'},
        {'fisrtname': 'Miguel','lastname': 'Torres'},
        {'fisrtname': 'Jessie','lastname': 'Amortegui'},
        {'fisrtname': 'Teresa','lastname': 'Prieto'}
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5],
        'integer_nums': [-1, -2, 0, 1,2],
        'floating_nums': [1.1, 4.5, 6.43]
    }

    # for key, value in super_dict.items():
    #     print(key, '-', value)

    # for i in super_list:
    #     print(i)

    for i in super_list:
        for key, values in i.items():
            print(key,'-', values)

    
        







if __name__ == '__main__':
    run()