from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, dump
import lxml.etree
from utils import prettify


class SaftGenerator:

    def __init__(self, root_tag):
        self.root = Element(root_tag)
        with open(f'xml-files/{root_tag}.xml', 'r') as f:
            for element in fromstring(f.read()).iter():
                if element.tag == root_tag: continue
                SubElement(self.root, element.tag)

    def add_sub_element(self, element_tag, inp=None):
        SubElement(self.root, element_tag).text = str(inp) if inp is not None else ''

    def fill_sub_element(self, tag, text):
        self.root.find(tag).text = str(text) if type(text).__name__ == 'int' else text

    def remove_sub_element(self, sub_element_tag):
        try:
            self.root.remove(self.root.find('softwareDesc'))
        except TypeError as e:
            print('STOOOOOR FEIL!!!', e)

    def print_tree(self):
        print(prettify(self.root))


if __name__ == '__main__':
    header = SaftGenerator('header')
    # test.add_sub_element('startDate', '2020-01-01')
    header.remove_sub_element('softwareDesc')

    header.print_tree()


