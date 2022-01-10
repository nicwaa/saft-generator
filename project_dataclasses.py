from typing import Optional
from pydantic import BaseModel, Extra
import enumerations as saft_enum


class CountryCodeFormatError(Exception):
    """
    Raises an error if the length and case of the string provided is incorrect
    """
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class ConfiguredBaseModel(BaseModel):

    class Config:
        extra = Extra.forbid


""" Data classes reflecting the xml elements required in the saft report """


class Header(ConfiguredBaseModel):
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

    class AuditfileSender(ConfiguredBaseModel):
        companyName: str
        companyIdent: Optional[str]
        taxRegistrationCountry: Optional[str]
        taxRegIdent: Optional[str]
        # streetAddress: Optional[object]
        # postalAddress: Optional[object]


class StreetAddress(ConfiguredBaseModel):
    streetname: Optional[str]
    number: Optional[str]
    additionalAddressDetails: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    region: Optional[str]
    country: Optional[saft_enum.CountryISOEnumeration]

    # @validator('country')
    # @classmethod
    # def country_valid(cls, value):
    #     if len(value) != 2 or value.islower():
    #         raise CountryCodeFormatError(value=value,
    #                                      message='Max string length: 2. Characters must be upper case. Example: NO')
    #     return value


class PostalAddress(ConfiguredBaseModel):
    streetname: Optional[str]
    number: Optional[str]
    additionalAddressDetails: Optional[str]
    city: str
    postalCode: str
    region: Optional[str]
    country: Optional[saft_enum.CountryISOEnumeration]

    # @validator('country')
    # @classmethod
    # def country_valid(cls, value):
    #     if len(value) != 2 or value.islower():
    #         raise CountryCodeFormatError(value=value,
    #                                      message='Max string length: 2. Characters must be upper case. Example: NO')
    #     return value


class Company(ConfiguredBaseModel):
    companyIdent: str
    companyName: str
    taxRegistrationCountry: Optional[str]
    taxRegIdent: Optional[str]


class CustomerSupplier(ConfiguredBaseModel):
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

    @staticmethod
    def base():
        return 'customersSuppliers'


class LedgerAccount(ConfiguredBaseModel):
    accID: str
    accDesc: str

    @staticmethod
    def base():
        return 'generalLedger'


class VatCodeDetail(ConfiguredBaseModel):
    vatCode: str
    dateOfEntry: str
    vatDesc: Optional[str]
    standardVatCode: str

    @staticmethod
    def base():
        return 'vatCodeDetails'


class Period(ConfiguredBaseModel):
    periodNumber: Optional[str]
    periodDesc: Optional[str]
    startDatePeriod: Optional[str]
    startTimePeriod: Optional[str]
    endDatePeriod: Optional[str]
    endTimePeriod: Optional[str]

    @staticmethod
    def base():
        return 'periods'


class Employee(ConfiguredBaseModel):
    empID: str
    dateOfEntry: str
    timeOfEntry: Optional[str]
    firstName: str

    @staticmethod
    def base():
        return 'employees'


class EmployeeRole(ConfiguredBaseModel):
    roleType: str
    roleTypeDesc: Optional[str]


class Article(ConfiguredBaseModel):
    artID: str
    dateOfEntry: str
    artGroupID: Optional[str]
    artDesc: str

    @staticmethod
    def base():
        return 'articles'


class Basic(ConfiguredBaseModel):
    basicType: saft_enum.BasicTypeEnumeration
    basicID: str
    predefinedBasicID: Optional[str]
    basicDesc: str

    @staticmethod
    def base():
        return 'basics'


class Location(ConfiguredBaseModel):
    name: str


class Cashregister(ConfiguredBaseModel):
    registerID: str
    regDesc: Optional[str]


class Event(ConfiguredBaseModel):
    eventID: str
    eventType: str
    transID: Optional[str]
    empID: Optional[str]
    eventDate: str
    eventTime: str
    eventText: Optional[str]


class EventReport(ConfiguredBaseModel):
    reportID: str
    reportType: saft_enum.ReportTypeEnumeration
    companyIdent: str
    companyName: str
    reportDate: str
    reportTime: str
    registerID: str

    class ReportTotalCashSales(ConfiguredBaseModel):
        totalCashSaleAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportArtGroup(ConfiguredBaseModel):
        artGroupID: str
        artGroupNum: str
        artGroupAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportArtGroups'

    class ReportEmpArtGroup(ConfiguredBaseModel):
        empID: str
        artGroupID: str
        artGroupNum: str
        artGroupAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportEmpArtGroups'

    class ReportPayment(ConfiguredBaseModel):
        paymentType: str
        paymentNum: str
        paymentAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportPayments'

    class ReportEmpPayment(ConfiguredBaseModel):
        empID: str
        paymentType: str
        paymentNum: str
        paymentAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportEmpPayments'

    class ReportTip(ConfiguredBaseModel):
        tipNum: str
        tipAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportCashSaleVat(ConfiguredBaseModel):
        vatCode: Optional[str]
        vatPerc: str
        cashSaleAmnt: str
        vatAmnt: str
        vatAmntTp: Optional[str]
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportCashSalesVat'

    class ReportEmpOpeningChangeFloat(ConfiguredBaseModel):
        empID: str
        openingChangeFloatAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportEmpOpeningChangeFloats'

    class ReportCorrLine(ConfiguredBaseModel):
        corrLineType: str
        corrLineNum: str
        corrLineAmnt: str

        @staticmethod
        def base():
            return 'reportCorrLines'

    class ReportPriceInquiry(ConfiguredBaseModel):
        priceInquiryGroup: str
        priceInquiryNum: str
        priceInquiryAmnt: str

        @staticmethod
        def base():
            return 'reportPriceInquiries'

    class ReportOtherCorr(ConfiguredBaseModel):
        otherCorrType: str
        otherCorrNum: str
        otherCorrAmnt: str

        @staticmethod
        def base():
            return 'reportOtherCorrs'

    class ReportCreditSales(ConfiguredBaseModel):
        creditSalesNum: str
        creditSalesAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportCreditMemos(ConfiguredBaseModel):
        creditMemosNum: str
        creditMemosAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportPayIn(ConfiguredBaseModel):
        payInType: str
        payInNum: str
        payInAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportPayIns'

    class ReportPayOut(ConfiguredBaseModel):
        payOutType: str
        payOutNum: str
        payOutAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportPayOuts'


class EventReportAfterCashSalesVat(ConfiguredBaseModel):
    reportOpeningChangeFloat: str
    reportReceiptNum: str
    reportOpenCashBoxNum: str
    reportReceiptCopyNum: str
    reportReceiptCopyAmnt: str
    reportReceiptProformaNum: str
    reportReceiptProformaAmnt: str
    reportReturnNum: str
    reportReturnAmnt: str
    reportDiscountNum: str
    reportDiscountAmnt: str
    reportVoidTransNum: str
    reportVoidTransAmnt: str

    def append_target(self):
        return 'eventReport'


class EventReportAfterReportOtherCorr(ConfiguredBaseModel):
    reportReceiptDeliveryNum: str
    reportReceiptDeliveryAmnt: str
    reportTrainingNum: str
    reportTrainingAmnt: str


class EventReportLast(ConfiguredBaseModel):
    reportGrandTotalSales: str
    reportGrandTotalReturn: str
    reportGrandTotalSalesNet: str


class Cashtransaction(ConfiguredBaseModel):
    nr: str
    transID: str
    transType: Optional[str]
    transAmntIn: str
    transAmntEx: str
    amntTp: saft_enum.DebitCreditEnumeration
    empID: Optional[str]
    custSupID: Optional[str]
    periodNumber: Optional[str]
    transDate: str
    transTime: str
    bookDate: Optional[str]
    bookTime: Optional[str]
    invoiceID: Optional[str]
    refID: Optional[str]
    desc: Optional[str]

    class CtLine(ConfiguredBaseModel):
        nr: str
        lineID: str
        lineType: str
        artGroupID: Optional[str]
        artID: Optional[str]
        qnt: Optional[str]
        lineAmntIn: str
        lineAmntEx: str
        amntTp: saft_enum.DebitCreditEnumeration
        ppu: Optional[str]
        costPrice: Optional[str]
        costID: Optional[str]
        costObjID: Optional[str]
        projID: Optional[str]
        empID: Optional[str]
        lineAmntInAccID: Optional[str]
        cashTransLineDescr: Optional[str]
        lineDate: Optional[str]
        lineTime: Optional[str]


class Vat(ConfiguredBaseModel):
    vatCode: Optional[str]
    vatPerc: Optional[str]
    vatAmnt: str
    vatAmntTp: Optional[str]
    vatBasAmnt: Optional[str]
    accID: Optional[str]


class Savings(ConfiguredBaseModel):
    savingsType: str
    savingsUnits: str
    empID: Optional[str]
    accID: Optional[str]


class Discount(ConfiguredBaseModel):
    dscTp: str
    dscAmnt: str
    empID: Optional[str]
    accID: Optional[str]


class Raise(ConfiguredBaseModel):
    raiseType: str
    raiseAmnt: str
    empID: Optional[str]
    accID: Optional[str]


class Rounding(ConfiguredBaseModel):
    roundingAmnt: Optional[str]
    accID: Optional[str]


class Payment(ConfiguredBaseModel):
    paymentType: str
    paidAmnt: str
    empID: Optional[str]
    curCode: Optional[str]
    exchRt: Optional[str]
    paymentRefID: Optional[str]
    accID: Optional[str]


class CashtransactionLast(ConfiguredBaseModel):
    signature: str
    keyVersion: str
    receiptNum: Optional[str]
    receiptCopyNum: Optional[str]
    receiptProformaNum: Optional[str]
    receiptDeliveryNum: Optional[str]
    voidTransaction: Optional[str]
    trainingID: Optional[str]
