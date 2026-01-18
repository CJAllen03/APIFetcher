# 🌍: Country Information Fetching Application
A Python command line input application that allows users to search for country information or filter certain sets of countries by category such as name, region, subregion, languages, or currency. The API that this application pulls information from is the REST Countries API (https://restcountries.com/).

## 📝: Features

### 👀: Search by Country Name: 
    Obtain detailed information for a specific country that includes:
      1) country's name
      2) capital
      3) region
      4) subregion
      5) population
      6) languages
      7) currencies
      8) nature of their independence.
     
      

  ### 🧭: Filtering Countries By:
    - Region    (e.g. Europe, Africa, Americas)
    - Subregion (e.g. North America, Southern Europe, Southern Africa)
    - Language (e.g. English, Spanish)
    - Currency (e.g. USD, Peso, Yen, Pound)
    
- Each Filter returns all matching countries and displays their country name, capital, and population 

### 🔁: The Interactive Loop
  -  ***The application will run continuously until the user types "exit" or "quit" notifying the system that they have concluded their search session.***
  
  -  This allows users to view and/or compare numerous datasets within a single session.

  ## 🧰: Requirements
  
    - The user must have access to Python Version 3.8+
    - Stable Internet Connection
    - Python's "requests" library 
    
  ### Install Dependencies

    pip install requests

  ## ⏯️ How to Run
  1)   Save the python script as shown in the below example:

    country_info.py
    
  2)   Run the Program:

     python country_info.py

  ## 💻: Usage
  ### Main Menu
    How would you like to access the Country data: Through Search or Filter?
    (Type 'exit' to quit)
  If search is entered then the next step would favor the following example:
    
    Enter Country Name: france      (input)
    
    Name: France
    Capital: Paris
    Region: Europe                          (output)
    Subregion: Western Europe
    Population: 67391582
    Languages: {'fra': 'French'}
    Currencies: {'EUR': {'name': 'Euro', 'symbol': '€'}}
    Independent?: True

However if filter is entered then the next step would favor this example:

    Which category would you like to filter by: Region, Subregion, Language, or Currency?
    region              (input)
    
    Enter the desired region:
    europe        (input)

    Name: France
    Capital: Paris
    Population: 67,391,582
                                (output)
    Name: Germany
    Capital: Berlin
    Population: 83,240,525

## :stop_sign: Special Input Handling
  -  Typing "exit" or "quit at most prompts exits the program or cancels the current action depending on your depth into the search
  -  Handles ambiguous input such as "no" for:
        -    Canceling a search
        -    Referring to United States Minor Outlying Islands
## 🏗️: Project Structure
    country-info-cli/
    │
    ├── country_info.py   # Main application script
    ├── README.md         # Project documentation
    
## 🌐: API Used
REST Countries API v3.1

Base URL: https://restcountries.com/v3.1/

Endpoints used:

-  /name/{country}

-  /region/{region}

-  /subregion/{subregion}

-  /lang/{language}

-  /currency/{currency}

## 📈: Possible Future Improvements 
-    Autocorrect for the country and category input. Could use the "from difflib import get_close_matches" library reference in Python
-    A sorting algorithm to sot information by population or in some Alphabetical order
-    Exporting the results to some Json file for better viewing
-    A graphical User Interface for improved readability and further its ease of use. (Maybe translate from Python to js and html for desired specifics)
-    Implement the features to be functionable across languages other than just English
