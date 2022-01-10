from generator import XmlGenerator
import project_dataclasses as pdc
from datetime import datetime

# Generate base tag
auditfile = XmlGenerator('auditfile')

# Generate header
# header = pdc.Header(
#     fiscalYear=datetime.now().year,
#     startDate='',
#     endDate='2020-01-31',
#     curCode='NOK',
#     dateCreated='2021-03-30',
#     timeCreated='10:40:00',
#     softwareDesc='Kassasystemet',
#     softwareVersion='3.14.1.3',
#     softwareCompanyName='Kassasystemer AS',
#     auditfileVersion='1.0'
# )
# auditfile.append(header)

auditfile.test()

print(auditfile)

with open('saft.xml', 'w') as f:
    f.write(str(auditfile))
