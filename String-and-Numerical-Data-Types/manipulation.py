# create a variable with a sentence from the user
str_manip = input("write a sentence : ")


# calculate characters in variable using len() and print
length_str_manip = len(str_manip)
print(length_str_manip)


# last letter location is -1
# print last letter by -1 for the start of the slice
last_str_manip = str_manip[-1:]
# replace the occurence of the last letter with @
print(str_manip.replace(last_str_manip, "@"))


# create variable with last 3 characters in str_manip
last3_str_manip = str_manip[-3:]
print(last3_str_manip)
# print last 3 characters backwards
print(last3_str_manip[::-1])


# create variable for first 3 characters in str_manip
first3_str_manip = str_manip[:3]
# create variable for last 2 characters in str_manip
last2_str_manip = str_manip[-2:]
# print the combined two above variables
print(first3_str_manip + last2_str_manip)