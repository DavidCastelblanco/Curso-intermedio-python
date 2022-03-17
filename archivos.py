def read():
    numbers = []
    with open ('./archivos/numbers.txt', 'r',encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['David', 'Jessie', 'Xime']
    with open ('./archivos/names.txt', 'w', encoding= 'utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')



def run():
    read()
    #write()


if __name__ =='__main__':
    run()