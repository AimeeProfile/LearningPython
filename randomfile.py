english = int(input("Enter your English exam percentage: "))
maths = int(input("Enter your Maths exam percentage: "))
science = int(input("Enter your Science exam percentage: "))
total_average = (english + maths + science)/3
print("Average exam percentage: ") 
print(total_average)
if total_average > 50: 
    print("Congratulations you passed!")
else:
     print("You failed :(") 

 

