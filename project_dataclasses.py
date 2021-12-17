from typing import Optional
from pydantic import BaseModel

""" Data classes reflecting the xml elements required in the saft report """


class Header(BaseModel):
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


class AuditfileSender(BaseModel):
    companyName: str
    companyIdent: Optional[str]
    taxRegistrationCountry: Optional[str]
    taxRegIdent: Optional[str]
    # streetAddress: Optional[object]
    # postalAddress: Optional[object]


class StreetAddress(BaseModel):
    streetname: Optional[str]
    number: Optional[str]
    additionalAddressDetails: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    region: Optional[str]
    country: Optional[str]


class PostalAddress(BaseModel):
    streetname: Optional[str]
    number: Optional[str]
    additionalAddressDetails: Optional[str]
    city: str
    postalCode: str
    region: Optional[str]
    country: Optional[str]


class Company(BaseModel):
    companyIdent: str
    companyName: str
    taxRegistrationCountry: Optional[str]
    taxRegIdent: Optional[str]


class CustomerSupplier(BaseModel):
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


class LedgerAccount(BaseModel):
    accID: str
    accDesc: str

    @staticmethod
    def base():
        return 'generalLedger'


class VatCodeDetail(BaseModel):
    vatCode: str
    dateOfEntry: str
    vatDesc: Optional[str]
    standardVatCode: str

    @staticmethod
    def base():
        return 'vatCodeDetails'


class Period(BaseModel):
    periodNumber: Optional[str]
    periodDesc: Optional[str]
    startDatePeriod: Optional[str]
    startTimePeriod: Optional[str]
    endDatePeriod: Optional[str]
    endTimePeriod: Optional[str]

    @staticmethod
    def base():
        return 'periods'


class Employee(BaseModel):
    empID: str
    dateOfEntry: str
    timeOfEntry: Optional[str]
    firstName: str

    @staticmethod
    def base():
        return 'employees'


class EmployeeRole(BaseModel):
    roleType: str
    roleTypeDesc: Optional[str]


class Article(BaseModel):
    artID: str
    dateOfEntry: str
    artGroupID: Optional[str]
    artDesc: str

    @staticmethod
    def base():
        return 'articles'


class Basic(BaseModel):
    basicType: str
    basicID: str
    predefinedBasicID: Optional[str]
    basicDesc: str

    @staticmethod
    def base():
        return 'basics'


class Location(BaseModel):
    name: str


class Cashregister(BaseModel):
    registerID: str
    regDesc: Optional[str]


class Event(BaseModel):
    eventID: str
    eventType: str
    transID: Optional[str]
    empID: Optional[str]
    eventDate: str
    eventTime: str
    eventText: Optional[str]


class EventReport(BaseModel):
    reportID: str
    reportType: str
    companyIdent: str
    companyName: str
    reportDate: str
    reportTime: str
    registerID: str

    class ReportTotalCashSales(BaseModel):
        totalCashSaleAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportArtGroup(BaseModel):
        artGroupID: str
        artGroupNum: str
        artGroupAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportArtGroups'

    class ReportEmpArtGroup(BaseModel):
        empID: str
        artGroupID: str
        artGroupNum: str
        artGroupAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportEmpArtGroups'

    class ReportPayment(BaseModel):
        paymentType: str
        paymentNum: str
        paymentAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportPayments'

    class ReportEmpPayment(BaseModel):
        empID: str
        paymentType: str
        paymentNum: str
        paymentAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportEmpPayments'

    class ReportTip(BaseModel):
        tipNum: str
        tipAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportCashSaleVat(BaseModel):
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

    class ReportEmpOpeningChangeFloat(BaseModel):
        empID: str
        openingChangeFloatAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportEmpOpeningChangeFloats'

    class ReportCorrLine(BaseModel):
        corrLineType: str
        corrLineNum: str
        corrLineAmnt: str

        @staticmethod
        def base():
            return 'reportCorrLines'

    class ReportPriceInquiry(BaseModel):
        priceInquiryGroup: str
        priceInquiryNum: str
        priceInquiryAmnt: str

        @staticmethod
        def base():
            return 'reportPriceInquiries'

    class ReportOtherCorr(BaseModel):
        otherCorrType: str
        otherCorrNum: str
        otherCorrAmnt: str

        @staticmethod
        def base():
            return 'reportOtherCorrs'

    class ReportCreditSales(BaseModel):
        creditSalesNum: str
        creditSalesAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportCreditMemos(BaseModel):
        creditMemosNum: str
        creditMemosAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

    class ReportPayIn(BaseModel):
        payInType: str
        payInNum: str
        payInAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportPayIns'

    class ReportPayOut(BaseModel):
        payOutType: str
        payOutNum: str
        payOutAmnt: str
        accID: Optional[str]
        accDesc: Optional[str]

        @staticmethod
        def base():
            return 'reportPayOuts'


class EventReportAfterCashSalesVat(BaseModel):
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


class EventReportAfterReportOtherCorr(BaseModel):
    reportReceiptDeliveryNum: str
    reportReceiptDeliveryAmnt: str
    reportTrainingNum: str
    reportTrainingAmnt: str


class EventReportLast(BaseModel):
    reportGrandTotalSales: str
    reportGrandTotalReturn: str
    reportGrandTotalSalesNet: str


class Cashtransaction(BaseModel):
    nr: str
    transID: str
    transType: Optional[str]
    transAmntIn: str
    transAmntEx: str
    amntTp: str
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

    class CtLine(BaseModel):
        nr: str
        lineID: str
        lineType: str
        artGroupID: Optional[str]
        artID: Optional[str]
        qnt: Optional[str]
        lineAmntIn: str
        lineAmntEx: str
        amntTp: str
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


class Vat(BaseModel):
    vatCode: str
    vatPerc: str
    vatAmnt: Optional[str]
    vatAmntTp: str
    vatBasAmnt: str
    accID: str


class Savings(BaseModel):
    savingsType: str
    savingsUnits: str
    empID: Optional[str]
    accID: Optional[str]


class Discount(BaseModel):
    dscTp: str
    dscAmnt: str
    empID: Optional[str]
    accID: Optional[str]


class Raise(BaseModel):
    raiseType: str
    raiseAmnt: str
    empID: Optional[str]
    accID: Optional[str]


class Rounding(BaseModel):
    roundingAmnt: Optional[str]
    accID: Optional[str]


class Payment(BaseModel):
    paymentType: str
    paidAmnt: str
    empID: Optional[str]
    curCode: Optional[str]
    exchRt: Optional[str]
    paymentRefID: Optional[str]
    accID: Optional[str]


class CashtransactionLast(BaseModel):
    signature: str
    keyVersion: str
    receiptNum: Optional[str]
    receiptCopyNum: Optional[str]
    receiptProformaNum: Optional[str]
    receiptDeliveryNum: Optional[str]
    voidTransaction: Optional[str]
    trainingID: Optional[str]


