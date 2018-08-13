from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

def indent(elem, level=0):
    i ="\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        # elif elem.text:
        #     elem.text = i + " "
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
subject.text="Why python?"
blog.append(subject)

author = Element("author")
author.text = "Eric"+"\n"+"  "
SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"
blog.append(author)

Agenda = Element("Agenda")
SubElement(Agenda, "from").text ="Jani"
SubElement(Agenda, "heading").text = "Reminder"
SubElement(Agenda, "body").text = "Don't forget me this weekend!"
blog.append(Agenda)

indent(blog)
dump(blog)

ElementTree(blog).write("blog.xml")
tree = parse("blog.xml")

subject_tag = blog.find("subject")
author_tags = blog.find("author")

print(subject_tag)
print(author_tags)

