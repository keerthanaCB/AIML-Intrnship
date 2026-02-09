total_bill=float(input("Enter Total bill amount:"))
print("Total bill amount is:",total_bill)
num_people=int(input("Enter number of people:"))
print("number of people is:",num_people)
if num_people > 0 :
    share = total_bill/num_people
    print("Total bill:",total_bill)
    print("Number of people:",num_people)
    print("Each person should pay:",round(share,2))
else:
    print("Number of people must be greaterthan 0")