from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

note = Element("note")
note.attrib["date"] = "20180108"
# note.attrib["editor"] = "pycharm"

to = Element("to")
to.text="Tove"
note.append(to)

SubElement(note,"to").text = "김인한"
SubElement(note,"to").text = "김기정"
SubElement(note,"to").text = "김상엽"


SubElement(note, "from").text ="Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

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

indent(note)
dump(note)
ElementTree(note).write("note.xml")

tree = parse("note.xml")
note = tree.getroot()

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
#
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
