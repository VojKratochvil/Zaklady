
import os

bidders = {}

print("Vítejte v pragramu na tichou aukci.")
lets_continue = "ano"

#plnění dictionary
while lets_continue == "ano":
    name = input(" Zadejte jméno:  ")
    bid = float(input("Zadejte cenovou nabídku:  "))
    bidders [name] = bid
    lets_continue = input("Někdo další ? ano/ne \n")
    if lets_continue == "ne":
        os.system("cls")

#high_bid = 0
#winner = ""  # hledání vítěze jéno je ten key
#for key in bidders:
#    if bidders[key] > high_bid:
#        high_bid = bidders[key]
#        winner = key
#print (f" Vítězem je {key} s nabídkou {high_bid}")

# jde to i jako funkce
def high_bid(bidders_dictionary):
    high_bid = 0
    winner = ""
    for key in bidders_dictionary:
        if bidders_dictionary[key] > high_bid:
            high_bid = bidders[key]
            winner = key


    #musí to být odsazený jinak to nepozná winera
    print (f" Vítězem je {winner} s nabídkou {high_bid}")

high_bid(bidders)

