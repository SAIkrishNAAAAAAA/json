#👉 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.




import json


indian_states_capitals = {
    "Telagana": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Kerala": "Trivandrum",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}


file_path = "indian_states_capitals.json"
with open(file_path, 'w') as json_file:
    json.dump(indian_states_capitals, json_file)

print("Data has been written to indian_states_capitals.json successfully.")





# Assignment 2
# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} is known for its hunting ability.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def special_ability(self):
        print(f"{self.name} is known for its strength and loyalty.")


if __name__ == "__main__":

    dog1 = Dog("Tommy", 3, "Brown")
    dog2 = Dog("Bolt", 5, "Black and White")

    
    dog1.description()
    dog1.get_info()

    dog2.description()
    dog2.get_info()

    jack_russell = JackRussellTerrier("Jackie", 2, "White with brown spots")
    bulldog = Bulldog("Rocky", 4, "Tan")

    
    jack_russell.description()
    jack_russell.get_info()
    jack_russell.special_ability()

    bulldog.description()
    bulldog.get_info()
    bulldog.special_ability()
