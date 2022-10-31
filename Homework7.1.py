import re
thing=input()
text=input()
s=re.findall(f'{thing}',text)
print(len(s))
