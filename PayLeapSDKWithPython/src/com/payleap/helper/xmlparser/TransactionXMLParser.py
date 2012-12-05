'''
Created on Oct 23, 2012

'''
from com.payleap.helper.xmlparser.Utility import Utility
import string

class TransactionXMLParser:
   
    def __init__(self, xmlStr):
        self.xmlStr = xmlStr
        self.resultStr = Utility.retriveFromXMLTag(xmlStr, "Result");
        try:
            self.result = int(self.resultStr)
        except Exception, e:
            print e
            self.result = -1
            
        self.respMSG = Utility.retriveFromXMLTag(xmlStr, "RespMSG");
        self.message = Utility.retriveFromXMLTag(xmlStr, "Message");
        self.message1 = Utility.retriveFromXMLTag(xmlStr, "Message1");
        self.message2 = Utility.retriveFromXMLTag(xmlStr, "Message2");
        
        if self.message is None or self.message == '':
            self.message = self.message1
        
        if self.message is None or self.message == '':
            self.message = self.message2
            
        self.authCode = Utility.retriveFromXMLTag(xmlStr, "AuthCode");
        self.PNRef = Utility.retriveFromXMLTag(xmlStr, "PNRef");
        self.hostCode = Utility.retriveFromXMLTag(xmlStr, "HostCode");
        self.hostURL = Utility.retriveFromXMLTag(xmlStr, "HostURL");
        self.receiptURL = Utility.retriveFromXMLTag(xmlStr, "ReceiptURL");
        self.getAVSResult = Utility.retriveFromXMLTag(xmlStr, "GetAVSResult");
        self.getAVSResultTXT = Utility.retriveFromXMLTag(xmlStr, "GetAVSResultTXT");
        self.getStreetMatchTXT = Utility.retriveFromXMLTag(xmlStr, "GetStreetMatchTXT");
        self.getZipMatchTXT = Utility.retriveFromXMLTag(xmlStr, "GetZipMatchTXT");
        self.getCVResult = Utility.retriveFromXMLTag(xmlStr, "GetCVResult");
        self.getCVResultTXT = Utility.retriveFromXMLTag(xmlStr, "GetCVResultTXT");
        self.getGetOrigResult = Utility.retriveFromXMLTag(xmlStr, "GetGetOrigResult");
        self.getCommercialCard = Utility.retriveFromXMLTag(xmlStr, "GetCommercialCard");
        self.workingKey = Utility.retriveFromXMLTag(xmlStr, "WorkingKey");
        self.keyPointer = Utility.retriveFromXMLTag(xmlStr, "KeyPointer");
        self.invNum = Utility.retriveFromXMLTag(xmlStr, "InvNum");
        self.cardType = Utility.retriveFromXMLTag(xmlStr, "CardType");
        self.extData = Utility.retriveFromXMLTag(xmlStr, "ExtData");
        self.tokenNumber = Utility.retriveFromXMLTag(xmlStr, "TokenNumber");   
        
       
    @staticmethod 
    def getValidateCardResponse(responseXmlStr):
        result = -1
        if responseXmlStr is not None:
            responseXmlStr = string.replace(responseXmlStr, " xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/\"", "", 1)
            resultStr = Utility.retriveFromXMLTag(responseXmlStr, "int");
            if resultStr is not None:
                try:
                    result = int(resultStr)
                except Exception, e:
                    print e
                    result = -1                    

            if result == 0:
                respMSG = "Approved";
            elif result == 1001:
                respMSG = "No card number present";
            elif result == 1002:
                respMSG = "No expiration date present";
            elif result == 1003:
                respMSG = "Invalid card type";
            elif result == 1004:
                respMSG = "Invalid card length";
            elif result == 1005:
                respMSG = "Invalid mod 10 check";
            elif result == 1006:
                respMSG = "Invalid expiration date";

        if result == -1:
            respMSG = "Invalid response";
        
        return respMSG;
    
    #===========================================================================
    # This method will process the validate card length response string and will return related response string
    #===========================================================================
    @staticmethod
    def getValidateCardLengthResponse(responseXmlStr):        
        try:            
            if responseXmlStr is not None:
                responseXmlStr = string.replace(responseXmlStr, " xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/\"", "", 1)
                resultStr = Utility.retriveFromXMLTag(responseXmlStr, "boolean");
                if "true" == resultStr:
                    return "Valid card length"
                elif "false" == resultStr:
                    return "Invalid card length"
                else:
                    return responseXmlStr
                
        except Exception, e:
            print e
            
        return "Empty reponse";
    
    #===========================================================================
    # This method will process the validate card length response string and will return related response string
    #===========================================================================
    @staticmethod
    def getValidateExpDateResponse(responseXmlStr):        
        try:           
            if responseXmlStr is not None:
                responseXmlStr = string.replace(responseXmlStr, " xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/\"", "", 1)
                resultStr = Utility.retriveFromXMLTag(responseXmlStr, "boolean");
                if "true" == resultStr:
                    return "Valid expiration date"
                elif "false" == resultStr:
                    return "Invalid expiration date"
                else:
                    return responseXmlStr
                
        except Exception, e:
            print e
            
        return "Empty reponse"
    
    
    #===========================================================================
    # This method will process the validate card length response string and will return related response string
    #===========================================================================
    @staticmethod
    def getValidMod10Response(responseXmlStr):        
        try:    
            if responseXmlStr is not None:
                responseXmlStr = string.replace(responseXmlStr, " xmlns=\"http://schemas.microsoft.com/2003/10/Serialization/\"", "", 1)
                resultStr = Utility.retriveFromXMLTag(responseXmlStr, "boolean");
                if "true" == resultStr:
                    return "Valid card number"
                elif "false" == resultStr:
                    return "Invalid card number"
                else:
                    return responseXmlStr
        except Exception, e:
            print e
            
        return "Empty reponse";
            

            
 

        
        



        
        


        