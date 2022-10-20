name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

if salary >= 3000:
    tax = salary * 21 / 100
elif salary >= 2000:
    tax = salary * 15 / 100
elif salary >= 1000:
    tax = salary * 10 / 100
else:
    tax = 0

net = salary - tax
print(name)
print(tax)
print(net)
