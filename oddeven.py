count = 0
while count < 9:
    count = count + 3
    remainder = count % 2
    if remainder == 1:
        print(count, "is even")
    else:
        print(count, "is odd")