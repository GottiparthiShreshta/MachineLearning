#QUESTION 2
#Creating an empty dictionary called dog - Dictionaries are represented as {} with key:value pairs.
dog = {}
print("Empty Dictionary")          #printing an empty dictionary
#Need to mention the key value pairs in " ", if they are strings.
dog["name"] = "Suri"               #adding the key as name and value as Suri to the dictionary
dog["color"] = "White"             #adding the key as color and value as White to the dictionary
dog["breed"] = "Shih Tzu"          #adding the key as breed and value as Shih Tzu to the dictionary
dog["legs"] = 4                    #adding the key as legs and value as 4 to the dictionary
dog["age"] = 2                     #adding key as age and value as 2 to the dictionary
print(dog)                         #Printing the dictionary after adding the key:value pairs.
Student_dict = {"first_name": "Shreshta", "last_name": "Gottiparthi", "gender": "F", "age": 23,
                "marital_status": "Single", "skills":["C", "Python"], "country": "India",
                "city": "Hyderabad", "address": "Himayatnagar, Telangana"}
print(Student_dict)
l = len(Student_dict)                                      #len() is used to get the length.
print("Length of Student_dict:", l)                             #we get the length of student dictionary
print("Items in skills:", Student_dict["skills"])        #this is to get the value of skills present in the student dictionary.
print("Type of Student_dict:", type(Student_dict["skills"]))  #type() is used to check the datatype. Checking the type of skills in the student
                                     #dictionary and printing the same.
Student_dict["skills"].append("SQL")                      #adding an extra element in the skills present in Student_dict
print("After adding an extra item:", Student_dict["skills"])
print("Keys in dictionary:", Student_dict.keys())         #using keys() to get all the keys aa a list.
print("Values in dictionary:", Student_dict.values())     #using values() to get all the values as a list.