input_strings = ["Banana", "Apple", "Watermelon", "Kiwi"]

for i in range(len(input_strings)):
    for j in range(i+1,len(input_strings)):
        if len(input_strings[i]) > len(input_strings[j]):
             input_strings[i],input_strings[j] = input_strings[j],input_strings[i]
 
print("sorted strings are: ", input_strings)    