divisable3 = []
divisable5 = []
summ = 0
ranges = int(input("Put in the number for the equation to mess with: "))

for x in range(ranges):
    if x % 3 == 0:
        divisable3.append(x)
    if x % 5 == 0:
        divisable3.append(x)
summ = sum(divisable3) + sum(divisable5)
print("The sum of all numbers equal to or under {} is {}".format(ranges, summ))
