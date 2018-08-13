import re

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")  ## ':' 은 소모하지 않는다. 맵핑만 시킨다.
m = p.search("http://google.com")
print(m.group())