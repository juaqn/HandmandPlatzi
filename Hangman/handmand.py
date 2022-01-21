from ast import get_source_segment
from calendar import c
from cgi import print_directory
from dataclasses import replace
import random  
import os
from urllib.parse import ParseResultBytes

def read():
    words = []
    with open('./archivos/data.txt','r', encoding='utf-8') as f: #read the flie provided
        for line in f:    
          words.append(line.strip().upper())
    #single_word = random.choice(words).upper() #pic a radom word
    return(words)

def normalize(s): # It removes the accents of a string
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
            ("Á", "A"),
            ("É", "E"),
            ("Í", "i"),
            ("Ó", "O"),
            ("Ú", "U"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

def chances(lifes, letra, secret, guess):
    test1 = guess
    if lifes == 0:
       return lifes
    else:
        for i in range(0,len(guess)):
            if secret[i] != letra or guess[i] != letra: 
                lifes -= 1
                return lifes
            else:
                
                return lifes
                


def hang(secret_word, the_word_is):
    secret = secret_word
    lines = the_word_is
    guess = ''.join(lines).upper()
    lifes = 11 
    keep_trying = True
    
    # while secret != lines or lifes > 0:
    while keep_trying:
        
        try: #This  improves performance
            letra = normalize(input('\nIngrese una(1) letra: ').upper())
            if letra == secret:
                print('Adivinaste!! la palabra era: '+str(secret).upper())
                keep_trying = False
            else:    
                assert letra.isalpha(), input('Solo se permiten letras , PRESIONE UNA TECLA PARA CONTINUAR')
                assert len(letra) == 1, input('Solo ingresar 1 no mas, PRESIONE UNA TECLA PARA CONTINUAR')
                
                for i in range(0,len(secret)):       
                    if secret[i] == letra:
                        lines[i] = secret[i]
                        guess = ''.join(lines).upper()
                  
                os.system('cls') #This line cleans the screen in every try  
                lifes = int(chances(lifes, letra, secret, guess))
                print('te quedan: ' + str(lifes) + ' oportunidades')
                print(guess)  
                        
          
                if guess == secret:
                    print('Adivinaste!! la palabra era: '+str(secret).upper())
                    keep_trying = False
                    
                if lifes == 0:
                    print('Perdiste!! la palabra era: '+str(secret).upper())
                    keep_trying = False
            

        except AssertionError as e:
            print(e)
            continue



def run():
    secret_word = random.choice(read()).upper()
    secret_word = normalize(secret_word)
    the_word_is = ['_' for letter in secret_word]
   

    print('Adivina la palapra: ')
    print(''.join(the_word_is))
    print('\n')

    hang(secret_word, the_word_is)
   


if __name__ == '__main__':
    run()
© 2022 GitHub, Inc.
Terms
Privacy
Security
