def leap(user_year):
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

        

def days(user_year, user_month):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_result = leap(user_year)
    if leap_result and user_month == 2: # leap result je boolean sám o sobě dává true nebo false 2 protže prestupny unor má 29 dní
        return 29
    else:
        return days_in_month[user_month - 1]

 
year = int(input("Jaký rok chcete zkontrolovat? "))
month = int(input("Zadejte měsíc "))
result = days(year, month)
prestupny = ""
# my vynález im fukin proud 
if leap(year) == True:
    prestupny = "je"
else:
    prestupny = "není"


print(f" Zvolený rok {prestupny} přestupný a počet dnů ve zvoleném měsíci je: {result}")
