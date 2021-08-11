blocks = int(input("Enter the number of blocks: "))
height = 0
for i in range(1, blocks):  # 1 2 3 4 5 
    height += i
    if height >= blocks:
        break
    print(i, height, end="\t")
print("\nThe height of the pyramid:", i)
# acum = 0
# while acum <= blocks:
#     height += 1

#heigth    blocks
#1          1 
#2          3       (3-1=2)
#3          6       (6-3=3)
#4          10      (10-6=4)
#5          15      (15-10=5)
#6          21      (21-15=6)
#    altura     número de bloques

#       #  1      1
#      ##  2      3
#     ###  3      6                     
#    ####  4     10
#   #####  5     15
#  ######  6     21                     1 - 2 - 3 - 4 
# la  última capa tiene 1 bloques
# cantidad de bloques  1     altura    1
# cantidad de bloques  3     altura    2
# cantidad de bloques  6     altura    3
# cantidad de bloques  10    altura    4
# cantidad de bloques  15    altura    5
# cantidad de bloques  21    altura    6