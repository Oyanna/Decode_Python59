countries = (
    ("Kazakhstan", 18000000, ("Astana", 5000000)),
    ("France", 50000000, ("Paris", 7000000))
)
for countries in countries:
    c_Name, c_population, capital = countries
    print("\nCountry: {} population: {}".format(c_Name, c_population))
    for city in capital:
        cityName, cityPopulation = capital
        print("City: {} population: {}".format(cityName, cityPopulation))


