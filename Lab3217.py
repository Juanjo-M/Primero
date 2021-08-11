# # break - example
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")

# continue - example

print("\nThe continue instruction:")
for i in range(1,10):
    if i > 4 and i < 8:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")