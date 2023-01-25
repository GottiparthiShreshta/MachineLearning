#QUESTION 9
N=int(input("Enter number of students:"))           #taking the input from the user.
students_weight_lbs=[]                              #empty list of weigth in lbs.
while(N):                                           #checking the condition by using while loop.
    students_weight_lbs.append(int(input()))
    N=N-1
students_weight_kgs=[]
for i in students_weight_lbs:                       #here, i is iterated through the list.
    students_weight_kgs.append(round(i*0.453,2))    #converting pounds to kgs
print("Student's weigth in kgs:", students_weight_kgs)
