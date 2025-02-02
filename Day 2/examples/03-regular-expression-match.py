# import re
# text = "The quick Brown fox with a brown tint and what a Brown."

# pattern = r"quick"
# match = re.match(pattern, text)

# if match:
#     print("Match found:", match.group())
# else:
#     print("Match not found")
    
    
import re

text = "The quick brown fox"
#original: pattern = r"quick"
pattern = r"The.*quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
    
# The re.match() function specifically looks for a match at the beginning of the string. In this case:
# The string starts with "The", not "quick".
# Although "quick" is present in the string, it's not at the beginning.