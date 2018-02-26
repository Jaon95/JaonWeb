import re

result = re.search(r'(?: [\w]+)','hello li')
print(result.group())