# <blog date= "20151231">
# <subject>Why python?</subject>
# <author>Eric</author>
#     <age>58</age>
#     <nation>USA</age>
# <Agenda>
#     <1.>Data Type</1.>
#     <2.>Controll Flow</2.>
#     <3.>Function</3.>
# </blog></Agenda>

from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

def indent(elem, level=0):
    i ="\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

blog = Element("blog")
blog.attrib["date"] = "20180108"

subject = Element("subject")
subject.text = "why python?"

author = Element("author")
author.text = "Eric"
SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"

Agenda = Element("Agenda")
SubElement(Agenda,"1.").text = "Data Type"
SubElement(Agenda,"2.").text = "Controll Flow"
SubElement(Agenda,"3.").text = "Function"

indent(blog)
dump(blog)

indent(subject)
dump(subject)

indent(author)
dump(author)

indent(Agenda)
dump(Agenda)
ElementTree(blog).write("blog.xml")

tree = parse("blog.xml")
#
#
# ElementTree(note).write("note.xml")
#
# tree = parse("note.xml")
# note = tree.getroot()
#
# print(note.get("date"))
# print(note.get("foo", "default"))
# print(note.keys())
# print(note.items())

# from_tag = note.find("from")
# print(from_tag)
# from_text = note.findtext("find")
# print(from_text)
#
# from_tags = note.findall("from") # ----> 333쪽 find의 인자 확인 findall은 전체
#
# to_tag = note.find("to")
# print(to_tag.test)
# to_tags = note.findall("to")
#
# for to_element in to_tags:
#     print(to_element.text)

# childs = note.getiterator()
# note.getiterator("from")

# print("Search from Root")
# for parent in note.getiterator():
#       for child in parent:
#           print(child.text)
#
# print("Search from from")
# for child in note.getiterator("from"):
#     print(child.text)
#
# print("end")