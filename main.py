
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, canonicalize, fromstring
from xml.dom.minidom import parseString
from generator import XmlGenerator
from utils import prettify

# Generate base tag
auditfile = XmlGenerator('auditfile')

# Generate header
header = XmlGenerator('header')
header.fill_sub_element('fiscalYear', 2020)
header.fill_sub_element('startDate', '2020-01-01')
header.fill_sub_element('endDate', '2020-01-31')
header.fill_sub_element('curCode', 'NOK')
header.fill_sub_element('dateCreated', '2021-03-30')
header.fill_sub_element('timeCreated', '10:40:00')
header.fill_sub_element('softwareDesc', 'Kassasystemet')
header.fill_sub_element('softwareVersion', '3.14.1.3')
header.fill_sub_element('softwareCompanyName', 'Kassasystemer AS')
header.fill_sub_element('auditfileVersion', '1.0')

auditfileSender = XmlGenerator('auditfileSender')
auditfileSender.fill_sub_element('taxRegistrationCountry', 'NO')
auditfileSender.fill_sub_element('companyName', 'big popo')

header.root.append(auditfileSender.root)
auditfile.root.append(header.root)

company = XmlGenerator('company')
company.append_sub_elements('customersSuppliers', 'customerSupplier')
auditfile.root.append(company.root)

auditfile.remove_sub_element('header')

print(auditfile)

with open('output.xml', 'w') as f:
    f.write(str(auditfile))
