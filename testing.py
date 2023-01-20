import requests



#print(data)
#search_name = input("What name do you want to check? ")

numbers = range(1,10)
for i in numbers:
    response = requests.get("https://swapi.dev/api/people/" + str(i) + "/")
    data = response.json()
    StarWarsNames = [data["name"]]
    print(StarWarsNames)