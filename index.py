import requests

#print(data)
search_name = input("What name do you want to check? ")
StarWarsNames = []
numbers = range(1,17)
for i in numbers:
    response = requests.get("https://swapi.dev/api/people/" + str(i) + "/")
    data = response.json()

    StarWarsNames.append(data["name"])
    


index = StarWarsNames.index(search_name)
index += 1

response = requests.get("https://swapi.dev/api/people/" + str(index) + "/")

data = response.json()

#This feels like a very roundabout way to get the homeworld of Luke Skywalker
#this might be able to be updated
homeworldString = data["homeworld"]
homeworld = requests.get(homeworldString)
homeworldActual = homeworld.json()

print(data["name"] + " is from " + 
 homeworldActual["name"] + 
 " and has the following attributes: " + "mass: " + "lbs" 
 + data["mass"] + ", height: " 
 + data["height"] 
 + ", hair_color: " 
 + data["hair_color"])



