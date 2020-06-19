import re

txt = "I have 21 Apples 1 banana"

x = re.findall("[0-9][0-9]", txt)

print(str(x))
