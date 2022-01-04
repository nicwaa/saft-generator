from xml.etree.ElementTree import tostring
from xml.dom.minidom import parseString


def prettify(elem):
    """ Return a pretty-printed XML string for the Element. """
    rough_string = tostring(elem, encoding='utf-8')
    reparsed = parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# big
# pp