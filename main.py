from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, canonicalize, fromstring
from xml.dom.minidom import parseString
from generator import XmlGenerator
import project_dataclasses as pdc

# Generate base tag
auditfile = XmlGenerator('auditfile')

# Generate header
header = XmlGenerator(
    pdc.Header(
        fiscalYear='2020',
        startDate='2020-01-01',
        endDate='2020-01-31',
        curCode='NOK',
        dateCreated='2021-03-30',
        timeCreated='10:40:00',
        softwareDesc='Kassasystemet',
        softwareVersion='3.14.1.3',
        softwareCompanyName='Kassasystemer AS',
        auditfileVersion='1.0'
    )
)
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

header.append(auditfileSender)
auditfile.append(header)

company = XmlGenerator('company')
company.append_to_sub_elements('customersSuppliers', 'customerSupplier')
auditfile.append(company)


print(auditfile)

with open('output.xml', 'w') as f:
    f.write(str(auditfile))
