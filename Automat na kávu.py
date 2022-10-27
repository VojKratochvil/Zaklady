from Source_data_automat_na_kavu import MENU
from Source_data_automat_na_kavu import resources

# Základní stuff
esspeso_price = MENU["espresso"]["cost"]


latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]

# Funkce


def report(data):
    print(f"Voda: {data['water']}"),
    print(f"Mléko: {data['milk']}"),
    print(f"Káva: {data['coffee']}"),


def coins():
    print("Vložte mince 10, 20 nebo 50 kč")
    kc1 = int(input("Kolik mincí o hodnotě 1 kč chcete vložit?: "))
    kc2 = 2 * int(input("Kolik mincí o hodnotě 2 kč chcete vložit?: "))
    kc5 = 5 * int(input("Kolik mincí o hodnotě 5 kč chcete vložit?: "))
    kc10 = 10 * int(input("Kolik mincí o hodnotě 10 kč chcete vložit?: "))
    kc20 = 20 * int(input("Kolik mincí o hodnotě 20 kč chcete vložit?: "))
    kc50 = 50 * int(input("Kolik mincí o hodnotě 50 kč chcete vložit?: "))
    money = kc1 + kc2 + kc5 + kc10 + kc20 + kc50
    print(f"Máte vloženo {money} Kč")
    return money


def change(user_money, price):
    refund = user_money - price
    if refund == 0:
        print("Nápoj se připravuje")
    elif refund > 0:
        print(f"Tady máte {refund} Kč nazpátek.")
    else:
        print(f"Nemáte dostatek peněz. Chybí Vám {price - user_money} Kč.")


def fill_ingredience():
    return resources


actual_resources = fill_ingredience()


def consumption_ingredience(name_of_drink, ingredience):
    if name_of_drink == "presíčko":
        name_of_drink = "espresso"
    elif name_of_drink == "kapůčo":
        name_of_drink = "cappuccino"
    ingredience["water"] = ingredience["water"] - MENU[name_of_drink]["ingredients"]["water"]
    ingredience["milk"] = ingredience["milk"] - MENU[name_of_drink]["ingredients"]["milk"]
    ingredience["coffee"] = ingredience["coffee"] - MENU[name_of_drink]["ingredients"]["coffee"]
    print(f"Zbylé ingredience: {ingredience}")

def ingredience_checker(in_water, in_milk, in_coffee):
    if in_water < 0:
        print("Nemáme dostatek vody na tento nápoj")
        return False
    elif in_milk < 0:
        print("Nemáme dostatek mléka na tento nápoj")
        return False
    elif in_coffee < 0:
        print("Nemáme dostatek kávy na tento nápoj")
        return False
    else:
        print("Ingrediencí je dostatek.")
        return True

def actual_ingredience(drink):
    if drink == "presíčko":
       consumption_ingredience(drink, actual_resources)
    elif drink == "latte":
        consumption_ingredience(drink, actual_resources)
    elif drink == "kapůčo":
        consumption_ingredience(drink, actual_resources)


lets_continue = True


# Kód
while(lets_continue):

    user_choice = input("Co si dáte? (presíčko/latte/kapůčo) ")

    actual_ingredience(user_choice)

    if user_choice != "report":
        lets_continue = ingredience_checker(actual_resources["water"], actual_resources["milk"], actual_resources["coffee"])

    # Kontola zda přerušit
    if lets_continue == False:
        break

    if user_choice == "report":
        report(actual_resources)

    if user_choice == "presíčko":
        print(f"Cena presíčka je {esspeso_price} Kč.")
        sum = coins()
        print(f"Cena presíčka je {esspeso_price} Kč.")
        change(sum, esspeso_price)
    elif user_choice == "latte":
        print(f"Cena latte je {latte_price} Kč.")
        sum = coins()
        print(f"Cena latte je {latte_price} Kč.")
        change(sum, latte_price)
    elif user_choice == "kapůčo":
        print(f"Cena kapůča je {cappuccino_price} Kč.")
        sum = coins()
        print(f"Cena kapůča je {cappuccino_price} Kč.")
        change(sum, cappuccino_price)
    else:
        print("Tento nápoj nevedeme. Vyberte si prosím, z nabídky.")

