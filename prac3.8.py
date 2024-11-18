my_dict = {"name": "Shelter", "age": 25}
my_dict["city"] = "Kumasi"
del my_dict["age"]

for key, value in my_dict.items():
    print(f"{key}: {value}")