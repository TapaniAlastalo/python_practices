countrycodes = [ "fi", "se", "no" ]

codemap = {
    "fi": "finland", 
    "se": "sweden",
    "no": "norway"
}

countries = {
    "finland": {
        "population": 5.439, 
        "head honcho": ("Juha Sipila", "54 years old")
    }, 
    "sweden": {
        "population": 9.593,
        "head honcho": ("Stefan Lofven", "58 years old")
    }, 
    "norway": {
        "population": 5.084,
        "head honcho": ("Erna Solberg", "54 years old")
    }
}

def printCountryInfo():
    for countrycode in countrycodes:
        #print(countrycode)
        #print(codemap[countrycode])
        #print(countries[codemap[countrycode]])
        country = codemap[countrycode]
        countryValues = countries[codemap[countrycode]]
        headHoncho = countryValues["head honcho"]
        population = countryValues["population"]
        print(country + ":")
        print("head honcho: " + headHoncho[0] + ", " + headHoncho[1])
        print("population: " + str(population) + " million")


printCountryInfo()