name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

if salary >= 1500:
    tax = salary * 21 / 100
else:
    tax = salary * 10 / 100

net = salary - tax

print(name)
print(tax)
print(net)