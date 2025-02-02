import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

#use str.split() for simple, fixed delimiter splits, and re.split() 
#when you need more complex splitting patterns or multiple delimiters
