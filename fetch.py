import requests

search_url = "https://restcountries.com/v3.1/name/"
category_url = "https://restcountries.com/v3.1/"

def searchCountry(name):
    #countryInfo = getCountryData(name)

    #mod_Url = f"{search_url}{name}?fullText=true&fields={name}"
    mod_Url = f"{search_url}{name}"
    response = requests.get(mod_Url)
    #print(response) checking for valid response

    if response.status_code == 200:
        country_Data = response.json() #converts data to python dictionary
        #return country_Data
        #print(country_Data)
        ##Lines for debugging to be sure that inputs are successfully taken
        #print("Data Successfully Gathered")
        #pass
    else:
        print(f"Failed to Obtain Country Data {response.status_code}")

    ##figuring out how to access specifics in this type of json format
    if country_Data:
        country_Data = country_Data[0]
        #print(f"{countryInfo}")
        print(f"Name: {country_Data["name"]["common"]}")
        print(f"Capital: {country_Data["capital"]}")
        print(f"Region: {country_Data["region"]}")
        print(f"Subregion: {country_Data["subregion"]}")
        print(f"Population: {country_Data["population"]}")
        print(f"Languages: {country_Data["languages"]}")
        print(f"Currencies: {country_Data["currencies"]}")
        print(f"Independent?: {country_Data["independent"]}")


def filterBy(category):
    if category == "region":
        category_id = input("Enter the desired region: ").lower()
        mod_Url = f"{category_url}{category}/{category_id}"
        response = requests.get(mod_Url)
        #print(response) 

        if response.status_code == 200:
            region_Data = response.json() #converts data to python dictionary
            #return country_Data
            #print(country_Data)
            ##Lines for debugging to be sure that inputs are successfully taken
            #print("Data Successfully Gathered")
            #pass
        else:
            print(f"Failed to Obtain Region Data {response.status_code}")

        ##figuring out how to access specifics in this type of json format

        for country in region_Data:
            name = country["name"]["common"]
            capital = country.get("capital", ["N/A"])[0]
            population = country.get("population", "N/A")

            print(f"Name: {name}")
            print(f"Capital: {capital}")
            print(f"Population: {population:,}")
            print("\n")
    elif category == "subregion":
        category_id = input("Enter the desired subregion: ").lower()
        mod_Url = f"{category_url}{category}/{category_id}"
        response = requests.get(mod_Url)
        #print(response) 

        if response.status_code == 200:
            subregion_Data = response.json() #converts data to python dictionary
            #return country_Data
            #print(country_Data)
            ##Lines for debugging to be sure that inputs are successfully taken
            #print("Data Successfully Gathered")
            #pass
        else:
            print(f"Failed to Obtain Subregion Data {response.status_code}")

        ##figuring out how to access specifics in this type of json format

        for country in subregion_Data:
            name = country["name"]["common"]
            capital = country.get("capital", ["N/A"])[0]
            population = country.get("population", "N/A")

            print(f"Name: {name}")
            print(f"Capital: {capital}")
            print(f"Population: {population:,}")
            print("\n")     
    elif category == "language":
        category = "lang"
        category_id = input("Enter the desired language: ").lower()
        mod_Url = f"{category_url}{category}/{category_id}"
        response = requests.get(mod_Url)
        #print(response) 

        if response.status_code == 200:
            language_Data = response.json() #converts data to python dictionary
            #return country_Data
            #print(country_Data)
            ##Lines for debugging to be sure that inputs are successfully taken
            #print("Data Successfully Gathered")
            #pass
        else:
            print(f"Failed to Obtain Language-Based Data {response.status_code}")

        ##figuring out how to access specifics in this type of json format

        for country in language_Data:
            name = country["name"]["common"]
            capital = country.get("capital", ["N/A"])[0]
            population = country.get("population", "N/A")

            print(f"Name: {name}")
            print(f"Capital: {capital}")
            print(f"Population: {population:,}")
            print("\n")
    elif category == "currency":
        category_id = input("Enter the desired currency: ").lower()
        mod_Url = f"{category_url}{category}/{category_id}"
        response = requests.get(mod_Url)
        #print(response) 

        if response.status_code == 200:
            currency_Data = response.json() #converts data to python dictionary
            #return country_Data
            #print(country_Data)
            ##Lines for debugging to be sure that inputs are successfully taken
            #print("Data Successfully Gathered")
            #pass
        else:
            print(f"Failed to Obtain Currency-Based Data {response.status_code}")

        ##figuring out how to access specifics in this type of json format

        for country in currency_Data:
            name = country["name"]["common"]
            capital = country.get("capital", ["N/A"])[0]
            population = country.get("population", "N/A")

            print(f"Name: {name}")
            print(f"Capital: {capital}")
            print(f"Population: {population:,}")
            print("\n")
    else:
        print("Not a Valid Category!\n")
        exit

while True:
    apiFeature = input("\nHow would you like to do access the Country data: Through Search or Filter? (Type 'exit' to quit)\n").lower()
    if apiFeature in ("exit", "quit"):
        print("Goodbye!")
        break
    elif apiFeature.lower() == "search":
        country_Name = input("Enter Country Name (or 'exit' to cancel): ").lower()
        if country_Name in ("exit", "quit"):
            continue
        if country_Name == "no":
            clarify_in = input("Did you mean no as in cancel the search or 'NO' as in US Outlying Islands: ").lower()
            if clarify_in in ("exit", "quit", "cancel"):
                continue
            if clarify_in == "no":
                exit
            elif clarify_in in ("us outlying islands","united states minor outlying islands","united states outlying islands"):
                searchCountry("united states minor outlying islands")
            else:
                print("Invalid entry for the posed question.")
                exit
        else:
            searchCountry(country_Name)
    elif apiFeature.lower() == "filter":
        prefCategory = input("Which category would you like to filter by: Region, Subregion, Language, or Currency? (or 'exit' to cancel)").lower()
        if prefCategory in ("exit", "quit"):
            continue
        filterBy(prefCategory)
    else:
        print("Invalid Access Path")
    ##figuring ou thow to access specifics in this type of json format

    secondStep = input("Would you like to compare/view another set of data? ")
    if secondStep in ("exit", "quit"):
            print("Goodbye!")
            continue
    if secondStep.lower() == "yes":
        apiFeature2 = input("How would you like to do access the second set of data: Through Search or Filter?\n")
        if apiFeature2.lower() == "search":
            country_Name2 = input("Enter Country Name: ").lower()
            if country_Name2 in ("exit", "quit"):
                continue
            if country_Name2 == "no":
                clarify_in2 = input("Did you mean no as in cancel the search or 'NO' as in US Outlying Islands: ").lower()
                if clarify_in2 in ("exit", "quit", "cancel"):
                    continue
                if clarify_in2 == "no":
                    exit
                elif clarify_in2 in ("us outlying islands","united states minor outlying islands","united states outlying islands"):
                    searchCountry("united states minor outlying islands")
                else:
                    print("Invalid entry for the posed question.")
                    exit
            else:
                searchCountry(country_Name2)
        elif apiFeature2.lower() == "filter":
            prefCategory2 = input("Which category would you like to filter by: Region, Subregion, Language, or Currency? ").lower()
            if prefCategory2 in ("exit", "quit"):
                continue
            filterBy(prefCategory2)
        else:
            print("Invalid Access Path")
    else:
        exit