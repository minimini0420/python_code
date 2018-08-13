import re
my_data = ""

# p = re.compile(r'(\b\w+)\s+\1')
# m = p.search("Paris in the the spring").group()
#
# data = """python one
# life is too short python two
# you need python
# python three"""
# print(p.findall(data))
# print(m)

# P_1 = re.compile(r'(\w+)\s+(\d+)[-](\d+)[-](\d+)')
# m_1 = P_1.search('yun 010-5333-4898')
# print(m_1.group(3))
#
# p = re.compile(r'(\w+)\s(\w+)\s\1\s\2')
#  m = p.search("sdf Hello World Hello World dkfhkdsfj")

p = re.compile(r"(\w+)\s(\w+)")
m = p.search("sdf Hello Hello ")
print(m)