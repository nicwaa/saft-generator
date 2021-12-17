from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, dump, ElementTree
from utils import prettify
from dataclasses import fields


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
            _root = _root.replace(_root[0], _root[0].lower())
            self.root = Element(_root)
            for tple in root:
                if tple[1] is not None:
                    SubElement(self.root, tple[0]).text = tple[1]

    def __repr__(self):
        return prettify(self.root)

    def add_sub_element(self, tag, text=None):
        SubElement(self.root, tag).text = str(text) if text is not None else ''

    def fill_sub_element(self, tag, text):
        self.root.find(tag).text = str(text) if type(text).__name__ != 'str' else text

    def append(self, element):
        self.root.append(element.root)

    def append_to_sub_elements(self, target_tag, source):
        self.root.find(target_tag).append(XmlGenerator(source).root)

    def remove_sub_element(self, tag):
        try:
            self.root.remove(self.root.find(tag))
        except TypeError as e:
            print('ikke spis rå poteter', e)


if __name__ == '__main__':
    header = XmlGenerator('header')
    header.append_sub_elements('fiscalYear', 'header')

    print(header)

    # for i in header.root.iter():
    #     print(i.tag)


