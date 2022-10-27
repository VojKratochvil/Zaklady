

import random
import os


print("Vítejte ve hře: Uhodni skryté číslo.\nMyslím si číslo od 1 do 100")


def obtiznost():
    difficulty = input("Vyberte obtížnost: easy nebo hard: ")
    
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

secret_number = random.randint(1, 100)
print(secret_number)



def hadaci_hra():
    
    attemps = obtiznost()

    another_game = ""

    while attemps > 0:
        
        print(f"Zbyvající počet pokusu je {attemps}")
        guess = int(input("Hádejte číslo"))
        
        if guess < secret_number:
            print("Příliž nízké")
            attemps -= 1
        elif guess > secret_number:
            print("Příliž vysoké")
            attemps -= 1
        else:
            print("Gratuluji")
            another_game = input("Chccete hrát znovu ano nebo ne")
            

        if attemps == 0:
            print(f"Tentokrát to nevyšlo číslo bylo {secret_number}")   
            another_game = input("Chccete hrát znovu ano nebo ne")
        
        if another_game == "ano":
            os.system("cls")
            hadaci_hra()
        elif another_game == "no":
            print("Díky za hru")
            os.system("cls")
            break

hadaci_hra()

