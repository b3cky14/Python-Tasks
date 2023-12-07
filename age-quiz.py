#create variable for users age
age = int(input("How old are you? "))

#age greater than or equal 40 but less than 65 over the hill
if age >= 40 and age < 65:
    print("You're over the hill.")
#age greater than 100 dead
elif age > 100:
    print("Sorry, you're dead.")
#age greater than or equal 65 but less than or equal 100 retirement
elif age >= 65 and age <= 100:
    print("Enjoy your retirement!")
#age less than 13 but greater than or equal to 0 kiddie
elif age < 13 and age >= 0:
    print("You qualify for the kiddie discount.")
#age equals 21 21st! (remember equals is double ==)
elif age == 21:
    print("Congrats on your 21st!")
#age equals anything else age is but a number
else:
    print("Age is but a number.")