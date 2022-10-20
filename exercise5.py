a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

if a > b and a > c:
    print("a", a)
elif a > b and a < c:
    print("c", c)
elif a < b and b > c:
    print("b", b)
else:
    print("c", c)