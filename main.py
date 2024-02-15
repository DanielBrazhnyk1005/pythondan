# task1
number = int(input("Enter 3 digits number : "))
n1 = number // 100
n2 = number // 10 % 10
n3 = number % 10
maxdigit = 0
mindigit =0
if n1 >= n2 and n1 >= n3:
    maxdigit = n1
if n2 >= n1 and n2 >= n3:
    maxdigit = n2
if n3 > n1 and n3 > n2:
    maxdigit = n3
if n1<=n2 and n1<=n3:
    mindigit = n1
if n2<=n1 and n2<=n3:
    mindigit = n2
if n3<=n1 and n3<=n2:
    mindigit = n3

average = (n1 + n2 + n3) / 3
print("Press 1 to see Max, 2 to see Min, 3 to see average")
Option = int(input("Please choose the options : "))

if Option == 1:
    print(maxdigit)
if Option == 2:
    print(mindigit)
if Option == 3:
    print(average)

# task 2

meters = int(input("Enter length in meters : "))
miles = meters * 0.000621
yards = meters * 1.093613
inches = meters * 39.36
print("Pick the option")
pick = int(input("Please choose the system : #1 miles; #2 yards; #3 inches "))
if pick == 1:
    print(miles)
if pick == 2:
    print(yards)
if pick == 3:
    print(inches)