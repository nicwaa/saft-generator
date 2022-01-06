from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, dump, ElementTree


class XmlGenerator:

    audit_attr = {
        'xmlns': "urn:StandardAuditFile-Taxation-CashRegister:NO",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xsi:schemaLocation': "urn:StandardAuditFile-Taxation-CashRegister:NO saft.xsd"
    }

    def __init__(self, root):
        if root == 'auditfile':
            self.root = Element(root, attrib=self.audit_attr)
        else:
            _root = root.__class__.__name__
            if _root[0].isupper():
                _root = _root[0].lower() + _root[1:]
            self.root = Element(_root)
            for tple in root:
                if tple[1] is not None:
                    SubElement(self.root, tple[0]).text = tple[1]

    def __repr__(self):
        return self.prettify(self.root)

    def add_sub_element(self, tag, _text=None):
        SubElement(self.root, tag).text = str(_text) if _text is not None else ''

    def fill_sub_element(self, tag, text):
        self.root.find(tag).text = str(text) if type(text).__name__ != 'str' else text

    def append(self, *args):
        for element in args:
            if element.__class__ == self.__class__:
                self.root.append(element.root)
            else:
                self.root.append(XmlGenerator(element).root)

    def meta_append(self, *args):
        for element in args:
            for tple in element:
                if tple[1] is not None:
                    self.add_sub_element(tple[0], tple[1])

    def append_to_tag(self, target_tag, *args):
        for element in args:
            if element.__class__ == self.__class__:
                self.root.find(target_tag).append(element.root)
            else:
                self.root.find(target_tag).append(XmlGenerator(element).root)

    def remove_sub_element(self, tag):
        try:
            self.root.remove(self.root.find(tag))
        except TypeError as e:
            print("Couldn't find the specified element tag.", e)

    @staticmethod
    def prettify(elem):
        """
        Return a pretty-printed XML string of the Element.
        """
        rough_string = tostring(elem, encoding='utf-8')
        reparsed = parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")


if __name__ == '__main__':
    header = XmlGenerator('header')
    header.append_to_tag('fiscalYear', header)

    print(header)

    # for i in header.root.iter():
    #     print(i.tag)