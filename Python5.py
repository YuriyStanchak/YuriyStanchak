z = input("enter z")
x = input("enter x")
y = input("enter y")
if z > x:
    print("good")
elif z < x:
    print("Try again")
elif z == x:
    if x < y:
        print("Try again")
    elif z < x:
        print("good")

