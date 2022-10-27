# nesting - něco v něčem (v hnízdečku) 
cities = {
    "Spain": "Madrid",
    "France": "Paris",
    
}

#print(cities["Spain"])

#list v dictionary
#travel_diary = {
#    "Spain": ["Madrid", "Leon", "Valencia"],
#    "France": ["Paris", "Nice", "Renes"]
#}
#print(travel_diary["France"][0])

travel_diary = {
    "Spain": {"visited_cities": ["Madrid", "Leon", "Valencia"], "visits" : 5},
    "France": {"visited_cities": ["Paris", "Nice", "Renes"], "visits": 2}
}
#print(travel_diary["France"]["visited_cities"][1])

#dictionary v listu
diary = [
    {
     "counry": "Spain",
     "visited_cities": ["Madrid", "Leon", "Valencia"], "visits" : 5,
    }, # nezapomenout na zkurvený čárky u dictionary
    {
     "counry": "France",
     "visited_cities": ["Paris", "Nice", "Renes"], "visits": 2  
    }
]

#print(diary[0]["visited_cities"][0])

#funkce pro přidání nové destinace
def add_country(country_name, cities, visits_number):
    new_dictionary = {}
    new_dictionary["country"] = country_name
    new_dictionary["visited_cities"] = cities
    new_dictionary["visits"] = visits_number
    diary.append(new_dictionary)

add_country("Italy", ["rome, Milano"], 9)  

print(diary[2]["visits"])