
# slovníky - nezáleží na pořadí -->u listu ano


#it_dictionary = {
#    "String": "Text",
#    "Integer": "Cele čislo",
#    "Float": "Desetinne čislo",
#    "Boolean": "Ano/ne"
#}

#print(it_dictionary["String"])

#it_dictionary2 = {
#    0: "Text",
#    1: "Cele čislo",
#    2: "Desetinne čislo",
#    3: "Ano/ne"
#}
#print(it_dictionary2[0])

#it_dictionary2[3] = "přidání hodnoty nebo změna pokud je již obsazeno"
#it_dictionary2[5] = "přidání hodnoty nebo změna pokud je již obsazeno"
#print(it_dictionary2)

#it_dictionary2 = {} #vyprázdnění slovníku
#print(it_dictionary2)


# můžu i vypsat hodnoty přes cyklus (for)
#for key in it_dictionary:
#    print(it_dictionary[key])


student_results = {
    "Harry": 85,
    "Ron": 71,
    "Hermiona": 98,
    "Draco": 69
}
description_result = {}
for key in student_results:
    result = ""
    score = student_results[key]
    if score >=91:
        result = "Excelentní"
    elif score >=81 and score <= 90:
        result = "Vynikající"
    elif score >=71 and score <= 80:
        result = "Splněno"
    elif score >=61 and score <= 70:
        result = "Nesplněno"
    description_result[key] = result

print(description_result)