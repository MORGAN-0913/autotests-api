import xml.etree.ElementTree as ET

xml_dat = """
<user>
    <name>Vasya</name>
    <age>30</age>
    <address>
        <city>Moscow</city>
        <street>Polyan</street>
        <house>1a</house>
    </address>
</user>
"""

root = ET.fromstring(xml_dat)

print(root.find("name").text)
