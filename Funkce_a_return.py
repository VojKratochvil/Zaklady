

#def sum(number1, number2):
#    print(number1 + number2)

#sum(5, 10)

def better_name(first_name, second_name):
    if first_name == "" or second_name == "":
        return " Nebylo zadáno jmeno nebo prijmeni " # pokud je nesmyslný imput dál to nepojede
    # za return se to nedava do zavorek
    first_name = first_name.capitalize() + " "
    second_name = second_name.capitalize()
    return f"{first_name}{second_name}" #na return končí to zatím se neprovede
    print("vypiš mě")

result = better_name(input("Jmeno"), input("Prijmeni"))

print(result)