import re

## p320 -- 그룹핑된 문자열에 이름 붙이기
print("첫번째 그룹 이름 활용")
p = re.compile(r"(?P<greeting>\w+)\s\1")
m = p.search("sdf Hello Hello")
print(m.group("greeting"))

print("\n두번째 그룹 이름 활용")
p = re.compile(r"(?P<greeting>\w+)\s(?P<destination>\w+)\s\1\s\2")
m = p.search("sdf Hello World Hello World dkfjkdsfj ")
print(m)

print(m.group("greeting"))
print(m.group("destination"))