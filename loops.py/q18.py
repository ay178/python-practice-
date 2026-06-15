"""Ask a number from the user, print the multiplication table upto 10"""
num=int(input("enter the number:-"))
i=1
while i<=10:
    print(f"{num} * {i} = {i*num}")
    i+=1