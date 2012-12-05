'''
Created on Oct 29, 2012

'''
from xml.dom import minidom, Node
import re

class GetCheckTrxRespParser:
    
    def __init__(self, node):
        
        self.Trx_HD_Key       = ""
        self.Invoice_ID       = ""
        self.Date_DT          = ""
        self.Merchant_Key     = ""
        self.Tuser_Name_VC    = ""
        self.Tip_Amt_MN       = ""
        self.Approval_Code_CH = ""
        self.Auth_Amt_MN      = ""
        self.Account_Type_CH  = ""
        self.Last_Update_DT   = ""
        self.Orig_TRX_HD_Key  = ""
        self.Result_CH        = ""
        self.Result_Txt_VC    = ""
        self.Settle_Date_DT   = ""
        self.Settle_Flag_CH   = ""
        self.Trans_Type_ID    = ""
        self.Void_Flag_CH     = ""
        self.CustomerID       = ""
        self.Avs_Resp_CH      = ""
        self.Cv_Resp_CH       = ""
        self.Host_Ref_Num_CH  = ""
        self.Zip_CH           = ""
        self.CheckNum_CH      = ""
        self.AccountNum_VC    = ""
        self.Total_Amt_MN     = ""
        self.NameOnCheck_VC   = ""
        self.TransitNum_VC    = ""
            
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue

            if child.tagName == 'TRX_HD_Key':
                self.Trx_HD_Key = self.gettext(child.childNodes)
            if child.tagName == 'Invoice_ID':
                self.Invoice_ID = self.gettext(child.childNodes)
            if child.tagName == 'Date_DT':
                self.Date_DT = self.gettext(child.childNodes)
            if child.tagName == 'Merchant_Key':
                self.Merchant_Key = self.gettext(child.childNodes)
            if child.tagName == 'Reseller_Key':
                self.Reseller_Key = self.gettext(child.childNodes)
            if child.tagName == 'TUser_Name_VC':
                self.Tuser_Name_VC = self.gettext(child.childNodes)
            if child.tagName == 'Processor_ID':
                self.Processor_ID = self.gettext(child.childNodes)
            if child.tagName == 'TRX_Settle_Key':
                self.TRX_Settle_Key = self.gettext(child.childNodes)
            if child.tagName == 'Tip_Amt_MN':
                self.Tip_Amt_MN = self.gettext(child.childNodes)
            if child.tagName == 'Approval_Code_CH':
                self.Approval_Code_CH = self.gettext(child.childNodes)
            if child.tagName == 'Auth_Amt_MN':
                self.Auth_Amt_MN = self.gettext(child.childNodes)
            if child.tagName == 'IP_VC':
                self.IP_VC = self.gettext(child.childNodes)
            if child.tagName == 'Account_Type_CH':
                self.Account_Type_CH = self.gettext(child.childNodes)
            if child.tagName == 'Last_Update_DT':
                self.Last_Update_DT = self.gettext(child.childNodes)
            if child.tagName == 'Orig_TRX_HD_Key':
                self.Orig_TRX_HD_Key = self.gettext(child.childNodes)
            if child.tagName == 'Result_CH':
                self.Result_CH = self.gettext(child.childNodes)
            if child.tagName == 'Result_Txt_VC':
                self.Result_Txt_VC = self.gettext(child.childNodes)
            if child.tagName == 'Settle_Date_DT':
                self.Settle_Date_DT = self.gettext(child.childNodes)
            if child.tagName == 'Settle_Flag_CH':
                self.Settle_Flag_CH = self.gettext(child.childNodes)
            if child.tagName == 'Trans_Type_ID':
                self.Trans_Type_ID = self.gettext(child.childNodes)
            if child.tagName == 'Void_Flag_CH':
                self.Void_Flag_CH = self.gettext(child.childNodes)
            if child.tagName == 'CustomerID':
                self.CustomerID = self.gettext(child.childNodes)
            if child.tagName == 'Avs_Resp_CH':
                self.Avs_Resp_CH = self.gettext(child.childNodes)
            if child.tagName == 'CV_Resp_CH':
                self.CV_Resp_CH = self.gettext(child.childNodes)
            if child.tagName == 'Host_Ref_Num_CH':
                self.Host_Ref_Num_CH = self.gettext(child.childNodes)
            if child.tagName == 'Zip_CH':
                self.Zip_CH = self.gettext(child.childNodes)
            if child.tagName == 'CheckNum_CH':
                self.CheckNum_CH = self.gettext(child.childNodes)
            if child.tagName == 'AccountNum_VC':
                self.AccountNum_VC = self.gettext(child.childNodes)
            if child.tagName == 'Total_Amt_MN':
                self.Total_Amt_MN = self.gettext(child.childNodes)
            if child.tagName == 'NameOnCheck_VC':
                self.NameOnCheck_VC = self.gettext(child.childNodes)
            if child.tagName == 'TransitNum_VC':
                self.TransitNum_VC = self.gettext(child.childNodes)
        
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
                for child in doc.getElementsByTagName("TrxDetailCheck"):
                    if child.nodeType != Node.ELEMENT_NODE:
                        continue
                    
                    checkTrxRespParser = GetCheckTrxRespParser(child);            
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
            
            
