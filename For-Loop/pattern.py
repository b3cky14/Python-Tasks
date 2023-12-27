# create variable for the string used in the pattern

string = "*"
  
# create for loop with a range

for i in range(1,10):
    if i <=5:
        print(i*string)         # 1,2,3,4,5 * string
    else:
        print((10-i)*string)      # 4,3,2,1 * string