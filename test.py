import re

result = re.findall(r'(\w+)(?: [\w]+)*','hello li')
print(result)

result = re.search(r'(\w+)?','sssssss')
print(result.group())