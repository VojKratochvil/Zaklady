

from cgi import print_directory
import os


def sum(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


operations = {
    "+": sum, #názvy funkce
    "-": sub,
    "*": mul,
    "/": div,
}
def kalkulacka():
    num1 = float(input("Zadejte první číslo: "))
    
    for symbol in operations:
        print(symbol)

    user_symbol = input("Zvolte operaci: ")

    num2 = float(input("Zadejte druhé číslo: "))

    calc_function = operations[user_symbol]
    result = calc_function(num1, num2)

    print(f"{num1} {user_symbol} {num2} = {result}")

    dalsi_cislo = input("Budete pokračovat? \nVypiš ""ano"" nebo ""ne ")
    if dalsi_cislo == "ano":
        while dalsi_cislo == "ano":
            num1 = result
            for symbol in operations:
                print(symbol)
            user_symbol = input("Zvolte operaci: ")
            num2 = float(input("Zadejte další číslo: "))

            calc_function = operations[user_symbol]
            result = calc_function(num1, num2)
            print(f"{num1} {user_symbol} {num2} = {result}")
            dalsi_cislo = input("Budete pokračovat? \nVypiš ""ano"" nebo ""ne ")
              
    elif dalsi_cislo == "ne":
        print("Děkuji za využití kalkulačky.")
        
    else: 
        print("Chyba v zadání příkazu pro pokračování.\nZačněte znovu a příště zadejte buď ano nebo ne ")
        kalkulacka()
    

kalkulacka()        
       
    




