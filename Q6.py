#QUESTION 6
x = "I am a teacher and I love to inspire and teach people"
y = x.split()                    #using split() to split the given sentence.
print("Sentence after splitting:", y)
#we convert this list to set to remove the duplicate elements
y = set(y)                       #set() is used to get the unique words from the list.
print("Unique words are:", y)
print("Number of unique words used:", len(y))
