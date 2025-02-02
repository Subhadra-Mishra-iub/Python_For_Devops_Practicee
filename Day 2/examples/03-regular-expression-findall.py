import re
text = "The quick Brown fox with a brown tint and what a Brown."
pattern = r"brown"

search = re.search(pattern, text)

if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


#Here the capslock matters
    