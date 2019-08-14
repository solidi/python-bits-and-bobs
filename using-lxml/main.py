from lxml import etree

root = etree.Element("root")
print(root.tag)
root.append(etree.Element("child1"))
root.append(etree.Element("child2"))
root.append(etree.Element("child3"))
print(etree.tostring(root, pretty_print=True))

child = root[0]
print(child.tag)
print(len(root))
children = list(root)

for child in root:
    print(child.tag)

root.insert(0, etree.Element("child0"))
start = root[:1]
end = root[-1:]

print(start[0].tag)
print(end[0].tag)
