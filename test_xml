import xml.etree.cElementTree as et

def load_xml (xml_file):
    tree = et.parse(xml_file)
    root = tree.getroot()
    strings = root.findall('string')
    o = file (r'c:/out.xml','w')
    j = 0
    for i in strings:
        j = j+1
        o.write('Line '+str(j)+' is: '+i.text.encode('utf-8')+'\n')

load_xml(r'c:/strings.xml')
