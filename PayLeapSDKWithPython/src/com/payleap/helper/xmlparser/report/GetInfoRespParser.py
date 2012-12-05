'''
Created on Oct 29, 2012

'''
from xml.dom import minidom, Node
import re

class GetInfoRespParser:
    
    def __init__(self, node):
        
        self.ExtData = ""
        self.Vendor = ""
        self.MerchantID = ""
        self.Phone1 = ""
        self.Phone2 = ""
        self.Auto_Close_Batch = ""
        self.CreditCard = ""
        self.PaymentTypes = ""
        self.CardType = ""
        self.RespMSG = ""
        self.Result = ""
            
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue

            if child.tagName == "ExtData":
                self.ExtData = self.gettext(child.childNodes)
            if child.tagName == "Vendor":
                self.Vendor = self.gettext(child.childNodes)
            if child.tagName == "MerchantID":
                self.MerchantID = self.gettext(child.childNodes)
            if child.tagName == "Phone1":
                self.Phone1 = self.gettext(child.childNodes)
            if child.tagName == "Phone2":
                self.Phone2 = self.gettext(child.childNodes)
            if child.tagName == "Auto_Close_Batch":
                self.Auto_Close_Batch = self.gettext(child.childNodes)
            if child.tagName == "CreditCard":
                self.CreditCard = self.gettext(child.childNodes)
            if child.tagName == "PaymentTypes":
                self.PaymentTypes = self.gettext(child.childNodes)
            if child.tagName == "CardType":
                self.CardType = self.gettext(child.childNodes)
            if child.tagName == "RespMSG":
                self.RespMSG = self.gettext(child.childNodes)
            if child.tagName == "Result":
                self.Result = self.gettext(child.childNodes)
        
    @staticmethod
    def parser(xmlStr):  
        try:  
            doc = minidom.parseString(xmlStr)
            
            #Checking for any errors
            errorNodes = doc.getElementsByTagName('ERROR')
            if(len(errorNodes) > 0):
                return errorNodes[0].firstChild.nodeValue
            else:
                objList = list()
                for child in doc.getElementsByTagName("Response"):
                    if child.nodeType != Node.ELEMENT_NODE:
                        continue
                    
                    checkTrxRespParser = GetInfoRespParser(child);            
                    objList.append(checkTrxRespParser);
                return objList
        except Exception, e:
            return e            
        #print "length: " , len(objList)
        #for item in objList:
        #    print "TRX_HD_Key: ", item.TRX_HD_Key

    def gettext(self, nodelist):
        retlist = []
        for node in nodelist:
            if node.nodeType == Node.TEXT_NODE:
                retlist.append(node.wholeText)
            elif node.hasChildNodes:
                retlist.append(self.gettext(node.childNodes))

        return re.sub('\s+', ' ', ''.join(retlist))
    
#l = GetCardTrxSummaryRespParser.parser("<string xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/\"><CardTrxSummary><PaymentMethod><Payment_Type_ID>VISA</Payment_Type_ID><Sale>25.12</Sale><Authorization>73.99</Authorization><PostAuth>0</PostAuth> <Return>0</Return><Capture>1E+25</Capture><TotalAmt>1E+25</TotalAmt><Sale_Cnt>6</Sale_Cnt><Authorization_Cnt>13</Authorization_Cnt><PostAuth_Cnt>0</PostAuth_Cnt><Return_Cnt>0</Return_Cnt><Capture_Cnt>96</Capture_Cnt><Cnt>115</Cnt></PaymentMethod></CardTrxSummary></string>");
#for item in l:
#    print "Payment_Type_ID: ", item.Payment_Type_ID
            
            
