physics_mark = int(input("Enter your physics mark: "))
chemistry_mark = int(input("Enter your chemistry mark: "))
maths_mark = int(input("Enter your maths mark: "))

total = physics_mark + chemistry_mark + maths_mark
percent = total / 450 * 100

if percent >=60:
    print("Pass")
else:
    print("Fail")
