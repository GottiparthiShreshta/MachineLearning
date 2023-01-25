#QUESTION 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
x = len(it_companies)                     #to get the length of it_companies set, we use len().
print("Length of the it_companies:", x)

#Adding 'Twitter' to it_companies set.
it_companies.add("Twitter")               #we use add() to add any element to a set.
print(it_companies)

#Inserting multiple IT companies at once to the set it_companies
it_companies.update(["Flipkart", "HP", "Wipro"]) #for adding multiple elements to a set, we use update().
print(it_companies)

#Removing one of the companies from the set it_companies
it_companies.remove("IBM")                 #use remove() for removing an element from the set.
print(it_companies)

#What is the difference between remove and discard
# The difference between remove() and dicard() is that the disacrd() method will not display any error if the specified
# item is not in the set. Whereas, remove() method will display an error.

#Joining A and B
C = A.union(B)                               #using union() method we get all the elements from both the sets.
print("After joining A and B:", C)

#Finding A intersection B
D = A.intersection(B)                        #returns a set which are common in both the sets A and B.
print("Intersection of A and B:", D)

#Is A subset of B
print("Is A subset of B?", A.issubset(B))    #checks if A is a subset of B, returns true if it is a subset else, returns false.

#Are A and B disjoint sets
print("Are A and B disjoint sets?", A.isdisjoint(B)) #checks if A and B are disjoints,if yes returns true else, false.

#Join A with B and B with A
X = A.copy() #copying the A set to X.
A.update(B)                                   #inserting all the ietms in B set to A set.
print("Joining A with B:", A)
B.update(X)                                   #inserting all the items in X set to B set.
print("Joining B with A:", B)

#What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
Y = A.symmetric_difference(B)                 #returns the set in which the items are not present in both the sets.
print("Symmetric Difference:", Y)

#Deleting the sets completely
del A
del B

#Convert the ages to a set and compare the length of the list and the set.
ages = set(age)                                           #converting the given list age to a set called ages using set().
print("After converting list to a set:", ages)
print("Length of a list- age:", len(age))                 #checking the length of a list.
print("Length of a set- ages:",len(ages))                 #checking the length of a set.









