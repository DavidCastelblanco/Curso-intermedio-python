import random
import unicodedata
import os

def words_list():
    words = []
    with open ('./archivos/data.txt', 'r',encoding='utf-8') as f:        
        for line in f:
            words.append(line)
    return words


def secret_word():
    secret_word_list =[]    
    list_of_words = words_list()
    secret_word_u = random.choice(list_of_words)    
    secret_word = unicodedata.normalize("NFKD", secret_word_u).encode("ascii","ignore").decode("ascii")
    secret_word_list = list(map(lambda i: secret_word[i], range(len(secret_word)-1)))

    return secret_word_list
 

    
def guess_word():
    
    word_to_guess_list = secret_word()
    secret_word_spaces = ''
    secret_word_letters = ''
    guess_word_list =[]
    new_word_spaces =''
    
    for i in range(len(word_to_guess_list)):
        secret_word_letters += word_to_guess_list[i]

    for i in word_to_guess_list:
        secret_word_spaces += '_ '

    guess_word_list =['_' for i in word_to_guess_list]

    
    print(word_to_guess_list)       

    while word_to_guess_list != guess_word_list:
        os.system ("cls")
        print('Vamos a jugar al ahorcado')
        print(secret_word_spaces)
        
        letter = input('Adivina una letra: ')
        
        for i in range(len(word_to_guess_list)):
            if letter == word_to_guess_list[i]:                
                guess_word_list[i]=letter
                new_word_spaces =''
                for i in range(len(guess_word_list)):
                    new_word_spaces += guess_word_list[i]+' '
                    secret_word_spaces = new_word_spaces
        
        
        
    os.system ("cls")
    print('FELICITACIONES, GANASTE!! la palabra era '+ secret_word_letters)
            


def run():

    
    guess_word()
   


if __name__ == '__main__':
    run()