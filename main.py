from read import readFile 
from operations import Property

properties = readFile("available_land.txt")

# for _property in properties:
#     print(_property)

# index = 0
# while index < len(properties):
#     index = index + 1

while True:

    print("""
            1: Display all properties
            2: Display available properties
            3: Rent property
            4: Return property
            5: Exit
        """)
    
    choice = int(input("Enter the choice: "))
    if choice == 1:
        for _property_key1 in properties.keys(): #dicitonary
            _property1 =properties.get(_property_key1)
            print(f"{_property1.kittaNumber} , {_property1.location}, {_property1.direction}, {_property1.anna}, {_property1.price}, {_property1.status}")
    elif choice == 2:
        for _property_key2 in properties.keys():
            _property2 = properties.get(_property_key2)
            if _property2.status == "Available":
                 print(f"{_property1.kittaNumber} , {_property1.location}, {_property1.direction}, {_property1.anna}, {_property1.price}, {_property1.status}")

    elif choice == 3:
        for _property_key2 in properties.keys():
            _property2 = properties.get(_property_key2)
            if _property2.status == "Available":
                print(f"{_property1.kittaNumber} , {_property1.location}, {_property1.direction}, {_property1.anna}, {_property1.price}, {_property1.status}")

        chosen_kitta_number = int(input("""
            Enter kitta number for Rent
            Press 0 to exit/cancel this process
        """))
        while chosen_kitta_number != 0:
            _property = properties.get(chosen_kitta_number)
            if _property != "Available":
                print("Not available for Rent ,choose another one!!!")
            else:
                _property.status = "Not Available"
                print(f"Price for property = {_property.price}")
                print(f"{_property1.kittaNumber} , {_property1.location}, {_property1.direction}, {_property1.anna}, {_property1.price}, {_property1.status}")
                break
    
        



