from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, dump
from utils import prettify
from dataclasses import dataclass, make_dataclass


class XmlGenerator:

    audit_attr = {
        'xmlns': "urn:StandardAuditFile-Taxation-CashRegister:NO",
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'xsi:schemaLocation': "urn:StandardAuditFile-Taxation-CashRegister:NO saft.xsd"
    }

    def __init__(self, root_tag):
        if root_tag == 'auditfile':
            self.root = Element(root_tag, attrib=self.audit_attr)
        else:
            self.root = Element(root_tag)
            with open(f'xml-templates/{root_tag}.xml', 'r') as f:
                for element in fromstring(f.read()).iter():
                    if element.tag == root_tag:
                        continue
                    SubElement(self.root, element.tag)

    def __repr__(self):
        return prettify(self.root)

    def add_sub_element(self, tag, text=None):
        SubElement(self.root, tag).text = str(text) if text is not None else ''

    def fill_sub_element(self, tag, text):
        self.root.find(tag).text = str(text) if type(text).__name__ != 'str' else text

    def append_sub_elements(self, target_tag, source_tag):
        self.root.find(target_tag).append(XmlGenerator(source_tag).root)

    def remove_sub_element(self, tag):
        try:
            self.root.remove(self.root.find(tag))
        except TypeError as e:
            print('ikke spis rå poteter', e)


if __name__ == '__main__':
    header = XmlGenerator('header')
    # test.add_sub_element('startDate', '2020-01-01')
    # header.remove_sub_element('timeCreated')
    header.append_sub_elements('fiscalYear', 'header')

    print(header)

    # for i in header.root.iter():
    #     print(i.tag)


