'''
Created on Oct 29, 2012

'''
from xml.dom import minidom, Node
import re

class GetOpenBatchSummaryRespParser:
    
    def __init__(self, node):
        
        self.Payment_Type_ID = ""
        self.Sale = ""
        self.Authorization = ""
        self.PostAuth = ""
        self.Return = ""
        self.Inquire = ""
        self.Capture = ""
        self.Reload = ""
        self.Activate = ""
        self.Sale_Cnt = ""
        self.Authorization_Cnt = ""
        self.PostAuth_Cnt = ""
        self.Return_Cnt = ""
        self.Capture_Cnt = ""
        self.Inquire_Cnt = ""
        self.Reload_Cnt = ""
        self.Activate_Cnt = ""
            
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue

            if child.tagName == "Payment_Type_ID":
                self.Payment_Type_ID = self.gettext(child.childNodes)
            if child.tagName == "Sale":
                self.Sale = self.gettext(child.childNodes)
            if child.tagName == "Authorization":
                self.Authorization = self.gettext(child.childNodes)
            if child.tagName == "PostAuth":
                self.PostAuth = self.gettext(child.childNodes)
            if child.tagName == "Return":
                self.Return = self.gettext(child.childNodes)
            if child.tagName == "Inquire":
                self.Inquire = self.gettext(child.childNodes)
            if child.tagName == "Capture":
                self.Capture = self.gettext(child.childNodes)
            if child.tagName == "Reload":
                self.Reload = self.gettext(child.childNodes)
            if child.tagName == "Activate":
                self.Activate = self.gettext(child.childNodes)
            if child.tagName == "Sale_Cnt":
                self.Sale_Cnt = self.gettext(child.childNodes)
            if child.tagName == "Authorization_Cnt":
                self.Authorization_Cnt = self.gettext(child.childNodes)
            if child.tagName == "PostAuth_Cnt":
                self.PostAuth_Cnt = self.gettext(child.childNodes)
            if child.tagName == "Return_Cnt":
                self.Return_Cnt = self.gettext(child.childNodes)
            if child.tagName == "Capture_Cnt":
                self.Capture_Cnt = self.gettext(child.childNodes)
            if child.tagName == "Inquire_Cnt":
                self.Inquire_Cnt = self.gettext(child.childNodes)
            if child.tagName == "Reload_Cnt":
                self.Reload_Cnt = self.gettext(child.childNodes)
            if child.tagName == "Activate_Cnt":
                self.Activate_Cnt = self.gettext(child.childNodes)
        
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
                for child in doc.getElementsByTagName("Table"):
                    if child.nodeType != Node.ELEMENT_NODE:
                        continue
                    
                    checkTrxRespParser = GetOpenBatchSummaryRespParser(child);            
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
            
            
