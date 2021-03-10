def main():
    class Pet:
        def __init__(self, name, animal_type, age):
            self.__name = name
            self.__animal_type = animal_type
            self.__age = age
        def set_name(self, name):
            self.__name = name
        def set_animal_type(self, animal_type):
            self.__animal_type = animal_type
        def set_age(self, age):
            self.__age = age
        def get_name(self):
            return self.__name
        def get_animal_type(self):
            return self.__animal_type
        def get_age(self):
            return self.__age
    name = input("What is your pet's name? ")
    animal_type = input("What type of animal is your pet? ")
    age = input("How old is your pet? ")
    my_pet = Pet(name, animal_type, age)
    print("Here is your pet's information:")
    print("Name:", my_pet.get_name())
    print("Type of animal:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())
main()