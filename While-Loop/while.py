# create variables for the input number, all the input numbers added together 
# and how many times the loop has happened

num = 0
add = 0
loop = 0

# while loop asking the user to input a number, 
# adding the input to the add variable and adding 1 to the loop variable

while num != -1:
    num = int(input("Pick a number : "))
    if num == -1:
        break           # break is used to stop the loop and exclude the -1 from the average calculation
    add += num
    loop += 1

# print the average of numbers entered
average = round(add/loop, 2)
print(f"The average of the numbers you enterer is {average}. This excludes your last entry of -1.")