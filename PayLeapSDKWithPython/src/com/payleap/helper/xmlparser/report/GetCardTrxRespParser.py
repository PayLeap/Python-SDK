'''
Created on Oct 29, 2012

'''
from xml.dom import minidom, Node
import re

class GetCardTrxRespParser:
    
    def __init__(self, node):
        
        self.TRX_HD_Key = ""
        self.Invoice_ID = ""
        self.Date_DT = ""
        self.Merchant_Key = ""
        self.TUser_Name_VC = ""
        self.Tip_Amt_MN = ""
        self.Approval_Code_CH = ""
        self.Auth_Amt_MN = ""
        self.Account_Type_CH = ""
        self.Last_Update_DT = ""
        self.Orig_TRX_HD_Key = ""
        self.Result_CH = ""
        self.Result_Txt_VC = ""
        self.Settle_Date_DT = ""
        self.Settle_Flag_CH = ""
        self.Trans_Type_ID = ""
        self.Void_Flag_CH = ""
        self.CustomerID = ""
        self.AVS_Resp_CH = ""
        self.CV_Resp_CH = ""
        self.Host_Ref_Num_CH = ""
        self.Zip_CH = ""
        self.Acct_Num_CH = ""
        self.Total_Amt_MN = ""
        self.Exp_CH = ""
        self.Name_on_Card_VC = ""
        self.Type_CH = ""
        self.Cash_Back_Amt_MN = ""
            
        for child in node.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue

            if child.tagName == 'TRX_HD_Key':
                self.TRX_HD_Key = self.gettext(child.childNodes)
            if child.tagName == 'Invoice_ID':
                self.Invoice_ID = self.gettext(child.childNodes)
            if child.tagName == 'Date_DT':
                self.Date_DT = self.gettext(child.childNodes)
            if child.tagName == 'Merchant_Key':
                self.Merchant_Key = self.gettext(child.childNodes)
            if child.tagName == 'TUser_Name_VC':
                self.TUser_Name_VC = self.gettext(child.childNodes)
            if child.tagName == 'Tip_Amt_MN':
                self.Tip_Amt_MN = self.gettext(child.childNodes)
            if child.tagName == 'Approval_Code_CH':
                self.Approval_Code_CH = self.gettext(child.childNodes)
            if child.tagName == 'Auth_Amt_MN':
                self.Auth_Amt_MN = self.gettext(child.childNodes)
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
            if child.tagName == 'AVS_Resp_CH':
                self.AVS_Resp_CH = self.gettext(child.childNodes)
            if child.tagName == 'CV_Resp_CH':
                self.CV_Resp_CH = self.gettext(child.childNodes)
            if child.tagName == 'Host_Ref_Num_CH':
                self.Host_Ref_Num_CH = self.gettext(child.childNodes)
            if child.tagName == 'Zip_CH':
                self.Zip_CH = self.gettext(child.childNodes)
            if child.tagName == 'Acct_Num_CH':
                self.Acct_Num_CH = self.gettext(child.childNodes)
            if child.tagName == 'Total_Amt_MN':
                self.Total_Amt_MN = self.gettext(child.childNodes)
            if child.tagName == 'Exp_CH':
                self.Exp_CH = self.gettext(child.childNodes)
            if child.tagName == 'Name_on_Card_VC':
                self.Name_on_Card_VC = self.gettext(child.childNodes)
            if child.tagName == 'Type_CH':
                self.Type_CH = self.gettext(child.childNodes)
            if child.tagName == 'Cash_Back_Amt_MN':
                self.Cash_Back_Amt_MN = self.gettext(child.childNodes)
        
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
                for child in doc.getElementsByTagName("TrxDetailCard"):
                    if child.nodeType != Node.ELEMENT_NODE:
                        continue
                    
                    cardTrxRespParser = GetCardTrxRespParser(child);            
                    objList.append(cardTrxRespParser);
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
    
#GetCardTrxRespParser.parser("<string xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/\"><RichDBDS><TrxDetailCard><TRX_HD_Key>14514</TRX_HD_Key><Invoice_ID></Invoice_ID><Date_DT>9/15/2011 11:53:03 AM</Date_DT><Merchant_Key>394</Merchant_Key><Reseller_Key>4</Reseller_Key><TUser_Name_VC>shoap123</TUser_Name_VC><Processor_ID>GiftCard Processor</Processor_ID><TRX_Settle_Key></TRX_Settle_Key><Tip_Amt_MN></Tip_Amt_MN><Approval_Code_CH></Approval_Code_CH><Auth_Amt_MN>1</Auth_Amt_MN><IP_VC>72.145.174.124</IP_VC><Account_Type_CH>MANUAL</Account_Type_CH><Last_Update_DT></Last_Update_DT><Orig_TRX_HD_Key></Orig_TRX_HD_Key><Result_CH>0</Result_CH><Result_Txt_VC>approval</Result_Txt_VC><Settle_Date_DT></Settle_Date_DT><Settle_Flag_CH>FALSE</Settle_Flag_CH><Trans_Type_ID>Sale</Trans_Type_ID><Void_Flag_CH>FALSE</Void_Flag_CH><CustomerID></CustomerID><AVS_Resp_CH>N</AVS_Resp_CH><CV_Resp_CH>S</CV_Resp_CH><Host_Ref_Num_CH>c3c7a40c-ae15-491f-82e2-aaba0f25e09c</Host_Ref_Num_CH><Zip_CH></Zip_CH><Acct_Num_CH>4111111111111111</Acct_Num_CH><Total_Amt_MN>1</Total_Amt_MN><Exp_CH>1215</Exp_CH><Name_on_Card_VC>GIFT</Name_on_Card_VC><Type_CH></Type_CH><Cash_Back_Amt_MN></Cash_Back_Amt_MN></TrxDetailCard><TrxDetailCard><TRX_HD_Key>14516</TRX_HD_Key><Invoice_ID></Invoice_ID><Date_DT>9/15/2011 11:53:44 AM</Date_DT><Merchant_Key>394</Merchant_Key><Reseller_Key>4</Reseller_Key><TUser_Name_VC>shoap123</TUser_Name_VC><Processor_ID>GiftCard Processor</Processor_ID><TRX_Settle_Key></TRX_Settle_Key><Tip_Amt_MN></Tip_Amt_MN><Approval_Code_CH></Approval_Code_CH><Auth_Amt_MN>1.01</Auth_Amt_MN><IP_VC>72.145.174.124</IP_VC><Account_Type_CH>MANUAL</Account_Type_CH><Last_Update_DT></Last_Update_DT><Orig_TRX_HD_Key></Orig_TRX_HD_Key><Result_CH>0</Result_CH><Result_Txt_VC>approval</Result_Txt_VC><Settle_Date_DT></Settle_Date_DT><Settle_Flag_CH>FALSE</Settle_Flag_CH><Trans_Type_ID>Sale</Trans_Type_ID><Void_Flag_CH>FALSE</Void_Flag_CH><CustomerID></CustomerID><AVS_Resp_CH>N</AVS_Resp_CH><CV_Resp_CH>S</CV_Resp_CH><Host_Ref_Num_CH>7a56be0b-dbb3-4d0c-b731-0298cc2efbc3</Host_Ref_Num_CH><Zip_CH></Zip_CH><Acct_Num_CH>4111111111111111</Acct_Num_CH><Total_Amt_MN>1.01</Total_Amt_MN><Exp_CH>1215</Exp_CH><Name_on_Card_VC>GIFT</Name_on_Card_VC><Type_CH></Type_CH><Cash_Back_Amt_MN></Cash_Back_Amt_MN></TrxDetailCard><TrxDetailCard><TRX_HD_Key>14517</TRX_HD_Key><Invoice_ID></Invoice_ID><Date_DT>9/15/2011 12:02:48 PM</Date_DT><Merchant_Key>394</Merchant_Key><Reseller_Key>4</Reseller_Key><TUser_Name_VC>shoap123</TUser_Name_VC><Processor_ID>GiftCard Processor</Processor_ID><TRX_Settle_Key></TRX_Settle_Key><Tip_Amt_MN></Tip_Amt_MN><Approval_Code_CH></Approval_Code_CH><Auth_Amt_MN>1.01</Auth_Amt_MN><IP_VC>72.145.174.124</IP_VC><Account_Type_CH>MANUAL</Account_Type_CH><Last_Update_DT></Last_Update_DT><Orig_TRX_HD_Key></Orig_TRX_HD_Key><Result_CH>0</Result_CH><Result_Txt_VC>approval</Result_Txt_VC><Settle_Date_DT></Settle_Date_DT><Settle_Flag_CH>FALSE</Settle_Flag_CH><Trans_Type_ID>Sale</Trans_Type_ID><Void_Flag_CH>FALSE</Void_Flag_CH><CustomerID></CustomerID><AVS_Resp_CH>N</AVS_Resp_CH><CV_Resp_CH>S</CV_Resp_CH><Host_Ref_Num_CH>2fbfa087-12ec-4157-966d-160a2bea44b4</Host_Ref_Num_CH><Zip_CH></Zip_CH><Acct_Num_CH>4111111111111111</Acct_Num_CH><Total_Amt_MN>1.01</Total_Amt_MN><Exp_CH>1215</Exp_CH><Name_on_Card_VC>GIFT</Name_on_Card_VC><Type_CH></Type_CH><Cash_Back_Amt_MN></Cash_Back_Amt_MN></TrxDetailCard><TrxDetailCard><TRX_HD_Key>14519</TRX_HD_Key><Invoice_ID></Invoice_ID><Date_DT>9/15/2011 12:03:48 PM</Date_DT><Merchant_Key>394</Merchant_Key><Reseller_Key>4</Reseller_Key><TUser_Name_VC>shoap123</TUser_Name_VC><Processor_ID>GiftCard Processor</Processor_ID><TRX_Settle_Key></TRX_Settle_Key><Tip_Amt_MN></Tip_Amt_MN><Approval_Code_CH></Approval_Code_CH><Auth_Amt_MN>1.02</Auth_Amt_MN><IP_VC>72.145.174.124</IP_VC><Account_Type_CH>MANUAL</Account_Type_CH><Last_Update_DT></Last_Update_DT><Orig_TRX_HD_Key></Orig_TRX_HD_Key><Result_CH>0</Result_CH><Result_Txt_VC>approval</Result_Txt_VC><Settle_Date_DT></Settle_Date_DT><Settle_Flag_CH>FALSE</Settle_Flag_CH><Trans_Type_ID>Sale</Trans_Type_ID><Void_Flag_CH>FALSE</Void_Flag_CH><CustomerID></CustomerID><AVS_Resp_CH>N</AVS_Resp_CH><CV_Resp_CH>S</CV_Resp_CH><Host_Ref_Num_CH>65652f1b-2671-4351-8214-a200a5a5d75b</Host_Ref_Num_CH><Zip_CH></Zip_CH><Acct_Num_CH>4111111111111111</Acct_Num_CH><Total_Amt_MN>1.02</Total_Amt_MN><Exp_CH>1215</Exp_CH><Name_on_Card_VC>GIFT</Name_on_Card_VC><Type_CH></Type_CH><Cash_Back_Amt_MN></Cash_Back_Amt_MN></TrxDetailCard></RichDBDS> </string>");
            
            
