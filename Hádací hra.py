import random


print("Tohle je hádací hra. Máš 2 pokusy")
charakters = ["Harry", "Ron", "Hermiona"]

charakter = charakters[random.randint(0, len(charakters)-1)]
guess = ""
guess_count = 2
while charakter != guess:
    if guess_count != 0:
        guess = input("Hádej postavu z HP\n")
        guess_count -= 1
    else:
        print(f"Nepovedlo se byl/a to {charakter}")
        break
    if charakter == guess:
       print(f"Gratuluji je to {charakter}") 

