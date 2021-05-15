"""We start with implementing the base class that the whole code will be based around"""
class Dog:
    def __init__(self, breed, age, mass):
        self.breed = breed
        self.age_in_years = age
        self.mass_in_kg = mass

    def __str__(self):
        return f"This {type(self).__name__.lower()} "\
        f"Is a breed of {self.breed} "\
        f"Is {self.age_in_years} years old and "\
        f"has a mass of {self.mass_in_kg} kilograms. "\

"""In the part above we have code part that will use the data we provide to
use it/fill the gaps we left in text/code"""
"""In the part below we implemented a subclass that has a bonus information about our dog, it's fur color"""

class Labrador(Dog):
    def __init__(self, breed, age, mass):
        super().__init__(breed, age, mass)
        self.fur_color = "white"
    def __str__(self):
        facts = super().__str__()
        facts = f"{facts} it also has a {self.fur_color} fur"
        return facts

"""below we add the information and call the program to do the rest"""
labrador = Labrador("Labrador", 3, 15)
print(labrador)