#QUESTION 3
#Creating a tuple containing names of sisters and brothers.
sisters =("Sneha", "Neha")
brothers = ("Rahul", "Varun", "Rohan")
#Joining the above two tuples and assigning it to a new tuple called siblings.
siblings = sisters+brothers                          #we use + to combine both the tuples.
print("Siblings are:", siblings)
s = len(siblings) #using len() to check the number of siblings present in the siblings tuple.
print("Number of siblings:", s)
#Tuples are immutable. We cannot modify a tuple!!
family_members = siblings+("Geeta","Venu")           #So here, I'm taking whole siblings tuple and adding the name of
                                                     #mother and father, assigning it to a new tuple called family_members.
print("Family Members:", family_members)