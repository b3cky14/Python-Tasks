#create variable for user time taken for swimming
swim = int(input("How many minutes did it take you to finish the swimming event? "))

#create variable for user time taken for cycling
bike = int(input("How many minutes did it take you to finish the cycling event? "))

#create variable for user time taken for running
run = int(input("How many minutes did it take you to finish the running event? "))

#create variable with all three events added together and print total time
total = swim + bike + run
print(f"The triathlon took you {total} minutes to finish.")

#if statement on total time greater than and equal to 111 minutes no award
if total >= 111:
    print("You have received no award.")

#elif statement 106-110 provincial scroll
elif total >= 106 and total <= 110:
    print("You have received the Provincial Scroll.")

#elif statement 101-105 provincial half colours
elif total >= 101 and total <= 105:
    print("You have received the Provincial Half Colours.")

#elif statement 0-100 provincial colours
elif total >= 0 and total <= 100:
    print("You have received the Provincial Colours.")

#else statement for inputs less than 0
else:
    print("You may have inputted your times incorrectly, please try again.")
