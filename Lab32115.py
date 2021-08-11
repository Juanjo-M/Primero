# c0 =  16
# c0 = c0/2    8  
# c0 = c0/2    4
# c0 = c0/2    2
# c0 = c0/2    1


# c0 = 15
# c0 = 3 * c0 + 1 = 3 * 15 + 1 = 45 + 1 = 46
# c0 = c0 / 2 = 46 / 2 = 23
# c0 = 3 * c0 + 1 = 3 * 23 + 1 = 70
# c0 = c0 / 2 = 70 / 2 = 35
# c0 = 3 * c0 + 1 = 3 * 35 + 1 = 106

c0 = int(input("ingrese un número natural: "))
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1 
    print(str(c0))
print("steps: " + str(steps))