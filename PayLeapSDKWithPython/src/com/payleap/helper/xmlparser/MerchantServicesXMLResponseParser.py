'''
Created on Oct 26, 2012

'''
from com.payleap.helper.xmlparser.Utility import Utility

class MerchantServicesXMLResponseParser:
    
    #===========================================================================
    # Used to populate JAVA response object from xml response string
    #===========================================================================
    def  __init__(self, xmlResponseString):
        self.ccInfoKey = Utility.retriveFromXMLTag(xmlResponseString, "CcInfoKey")
        self.code = Utility.retriveFromXMLTag(xmlResponseString, "Code")
        self.contractKey = Utility.retriveFromXMLTag(xmlResponseString, "ContractKey")
        self.customerKey = Utility.retriveFromXMLTag(xmlResponseString, "CustomerKey")
        self.error = Utility.retriveFromXMLTag(xmlResponseString, "Error")
        self.userName = Utility.retriveFromXMLTag(xmlResponseString, "UserName")
        self.vendor = Utility.retriveFromXMLTag(xmlResponseString, "Vendor")
        self.authCode = Utility.retriveFromXMLTag(xmlResponseString, "AuthCode")
        self.message = Utility.retriveFromXMLTag(xmlResponseString, "Message")
        self.pnref = Utility.retriveFromXMLTag(xmlResponseString, "PNRef")
        self.result = Utility.retriveFromXMLTag(xmlResponseString, "Result")
        self.checkInfoKey = Utility.retriveFromXMLTag(xmlResponseString, "CheckInfoKey")        
    