import re
input_str = input("Write something plz")
str1 = 's'
length_str = len(input_str)
if str1 in input_str:
    i = 0
    j = 0
    new_str = ''
    for i in range(0, length_str):
        #print(i)
        str2 = input_str[i]
        #print(str)
        #print(new_str)
        if re.match(str2, str1):
           i = i
        else:
            new_str = new_str + str2
            #print(new_str)
            i = i+1
    print(new_str)
else:
    print(input_str)

