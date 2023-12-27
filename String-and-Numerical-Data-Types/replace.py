# create variable containing the sentence
single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# replace ! with blank space using replace() function and print
replace_string = single_string.replace("!"," ")
print(replace_string)

# change string to upper case with upper(function) and print
upper_string = replace_string.upper()
print(upper_string)

# print sentence in reverse using slicing
print(single_string[::-1])