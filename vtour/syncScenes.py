import xml.etree.ElementTree
print("Hello World")
e = xml.etree.ElementTree.parse('tour.xml').getroot()

for scene in e.findall('scene'):
    print(scene.get('name'))
print(e)
