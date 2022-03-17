DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    }
]

def run():

    #Trabajadores que manejan python
    #Con list comprehansion
    all_python_devs = [worker['name'] for worker in DATA if worker['language']== 'python']

    #con high order funtions
    all_python_devs = list(filter(lambda x: x['language']== 'python', DATA))
    all_python_devs = list(map(lambda x: x['name'], all_python_devs))

    print('trabajadores que manejan python')    
    for worker in all_python_devs:
        print(worker)
    
    #Trabajadores que trabajan en Platzi
    #Con list comprehansion
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    #con high order functions
    all_platzi_workers = list(filter(lambda x: x['organization']=='Platzi', DATA))
    all_platzi_workers = list(map(lambda x: x['name'], all_platzi_workers))

    print('trabajadores de platzi')
    for worker in all_platzi_workers:
        print(worker)


    #Trabajadores mayores de edad

    #Con list comprehansion
    adults = [worker['name'] for worker in DATA if worker ['age']>18]

    #con high order functions
    adults = list(filter(lambda worker: worker['age']>18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))

    print('Trabajadores mayores de edad')
    for worker in adults:
        print(worker)

    #Crear lista con la llave old

    #con high order functions
    old = list(map(lambda worker: worker | {'old': worker['age']>70}, DATA))

    #Con list comprehansion
    old = [worker | {'old': worker['age']>70} for worker in DATA]

    print('Lista con llave old')
    for i in old:
        print(i)     

    

   

    


if __name__ == '__main__':
    run()