#QUESTION 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sorting the above list - using sort() method, we can directly sort the list in ascending or descending order.
ages.sort()
print("List after sorting", ages)

#Finding min and max ages - using min() and max() functions, we can find the min and max ages
x = min(ages) #storing minimum age in x
y = max(ages) #storing maximum age in y
print("Min age is:", x)
print("Max age is:", y)

#Adding min and max age again to the list - using append() method we can add the elements to the list.
ages.append(x)
ages.append(y)
print("After adding min and max ages to the list:", ages)

#After adding the ages again, I have again sorted the list for findind the median
ages.sort()
print("List after sorting again after adding ages", ages)

#Finding the median age
#getting length of ages list
a = len(ages)

#if-else condition to check length is even or odd
if(a%2 == 0):
    median = (ages[a//2] + ages[a//2-1])/2 #if even, take avg of middle two numbers as median
else:
    median = ages[n//2] #if odd, take middle number as median
print("Median is:", median)

#Finding the average age - sum of all ages divided by length of all ages.
average = sum(ages)/a
print("Average age:", average)

#Finding the range of ages - Subtracting the max age with min age.
print("Range of ages:", y-x)



