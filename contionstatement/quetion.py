"""
90 above -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
60 and below -> Fail 
"""
marks =int(input("enter marks = "))
if marks > 90 :
    print("Grade:A")
elif 90< marks >= 81:
    print("Grade:B")
elif 80<= marks >=71:
    print("Grade:C")
elif 70<= marks >=61:
    print('Grade:D')
else:
    print('fail')
    
