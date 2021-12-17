from typing import Optional
import pydantic

""" Data classes reflecting the xml elements required in the saft report """

class Header(pydantic.BaseModel):
    fiscalYear: str
    startDate: str
    endDate: str
    curCode: str
    dateCreated: str
    timeCreated: str
    softwareDesc: str
    softwareVersion: str
    softwareCompanyName: str
    auditfileVersion: str
    headerComment: Optional[str]
    userID: Optional[str]

class AuditfileSender(pydantic.BaseModel):
    companyName: str
    companyIdent: Optional[str]
    taxRegistrationCountry: Optional[str]
    taxRegIdent: Optional[str]
    # streetAddress: Optional[object]
    # postalAddress: Optional[object]

class StreetAddress(pydantic.BaseModel):
    streetname: Optional[str]
    number: Optional[str]
    additionalAddressDetails: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    region: Optional[str]
    country: Optional[str]

class PostalAddress(pydantic.BaseModel):
    streetname: Optional[str]
    number: Optional[str]
    additionalAddressDetails: Optional[str]
    city: str
    postalCode: str
    region: Optional[str]
    country: Optional[str]

class Company(pydantic.BaseModel):
    companyIdent: str
    companyName: str
    taxRegistrationCountry: Optional[str]
    taxRegIdent: Optional[str]

class CustomerSupplier(pydantic.BaseModel):
    custSupID: str
    custSupName: str
    custSupType: str
    contact: Optional[str]
    telephone: Optional[str]
    fax: Optional[str]
    eMail: Optional[str]
    website: Optional[str]
    taxRegistrationCountry: Optional[str]
    taxRegIdent: Optional[str]

class LedgerAccount(pydantic.BaseModel):
    accID: str
    accDesc: str

class VatCodeDetail(pydantic.BaseModel):
    vatCode: str
    dateOfEntry: str
    vatDesc: Optional[str]
    standardVatCode: str

class period(pydantic.BaseModel):
    periodNumber: Optional[str]
    periodDesc: Optional[str]
    startDatePeriod: Optional[str]
    startTimePeriod: Optional[str]
    endDatePeriod: Optional[str]
    endTimePeriod: Optional[str]

class employee(pydantic.BaseModel):
    empID: str
    dateOfEntry: str
    timeOfEntry: Optional[str]
    firstName: str

class employeeRole(pydantic.BaseModel):
    roleType: str
    roleTypeDesc: Optional[str]

class article(pydantic.BaseModel):
    artID: str
    dateOfEntry: str
    artGroupID: Optional[str]
    artDesc: str

class basic(pydantic.BaseModel):
    basicType: str
    basicID: str
    predefinedBasicID: Optional[str]
    basicDesc: str

class location(pydantic.BaseModel):
    name: str

class cashregister(pydantic.BaseModel):
    registerID: str
    regDesc: Optional[str]

class Event(pydantic.BaseModel):
    eventID: str
    eventType: str
    transID: Optional[str]
    empID: Optional[str]
    eventDate: str
    eventTime: str
    eventText: Optional[str]

class eventReport(pydantic.BaseModel):
(pydantic.BaseModel):
(pydantic.BaseModel):
(pydantic.BaseModel):