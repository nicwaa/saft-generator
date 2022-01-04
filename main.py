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

auditfile.append(header)


print(auditfile)

with open('output.xml', 'w') as f:
    f.write(str(auditfile))

# popo
