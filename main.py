
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, canonicalize, fromstring
from xml.dom.minidom import parseString
from generator import SaftGenerator
from utils import prettify

auditfile_attributes = {
    'xmlns': "urn:StandardAuditFile-Taxation-CashRegister:NO",
    'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'xsi:schemaLocation': "urn:StandardAuditFile-Taxation-CashRegister:NO saft.xsd"
}

auditfile = Element('auditfile', attrib=auditfile_attributes)

header = SaftGenerator('header')

header.fill_sub_element('fiscalYear', 2020)
header.fill_sub_element('startDate', '2020-1-1')
header.fill_sub_element('endDate', '2020-1-31')
header.fill_sub_element('curCode', 'NOK')
header.fill_sub_element('dateCreated', '2021-03-30')
header.fill_sub_element('timeCreated', '10:40:00')
header.fill_sub_element('softwareDesc', 'Kassasystemet')
header.fill_sub_element('softwareVersion', '3.14.1.3')
header.fill_sub_element('softwareCompanyName', 'Kassasystemer AS')
header.fill_sub_element('auditfileVersion', '1.0')

auditfileSender = SaftGenerator('auditfileSender')

header.root.append(auditfileSender.root)

auditfile.append(header.root)

print(prettify(auditfile))
#
# dump(auditfile)
#
# print(canonicalize(tostring(auditfile)))
#
with open('output.xml', 'wb') as f:
    f.write(prettify(auditfile).encode())
