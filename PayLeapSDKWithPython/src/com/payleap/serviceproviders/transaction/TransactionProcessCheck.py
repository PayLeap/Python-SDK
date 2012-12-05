'''
Created on Oct 25, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.TransactionXMLParser import TransactionXMLParser

class TransactionProcessCheck:
    """This class will help you to send a check transaction"""
    
    @staticmethod
    def processCheck(transType, checkNum, transitNum, accountNum, invNum, amount, micr, nameOnCheck, 
                 dl, ss, dob, stateCode, checkType, pnref, magdata, extData, serverMode):   
        r"""This method will help to build the ProcessCheck request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed. |br| 
            checkNum (str): The check number printed on the check. |br| 
            transitNum (str): The routing number printed on the check. |br| 
            accountNum (str): The account number printed on the check. |br| 
            invNum (str): Not used for this service. |br| 
            amount (str): The dollar amount of the transaction in DDDDDDDDDD.CC format. |br| 
            micr (str): The raw MICR data from the check in the following format. |br| 
            [TransitNum]T[AccountNum]O[CheckNum] |br| 
            Required only for the following SecCode values specified in ExtData: POP, BOC, ARC, C21 |br| 
            nameOnCheck (str): The customer's name as printed on the check. |br| 
            dl (str): The customer's driver's license number. Usage varies by check processor. |br| 
            ss (str): The customer's social security number. Usage varies by check processor. |br| 
            dob (str): The customer's date of birth in MM/DD/YYYY format. Usage varies by check processor. |br| 
            stateCode (str): The customer's two-digit driver's license state or province code. Usage varies by check processor. |br| 
            checkType (str): The type of bank account on which the check draws. Valid values are: |br| 
            Personal |br| 
            Corporate |br| 
            Government |br| 
            pnref (str): The PNRef number of the original sale transaction being refunded |br| 
            magdata (str):  |br| 
            extData (str): An XML string containing additional data for the transaction. See the following section for more information. |br|
            serverMode (str): Valid values are: PRODUCTION, UAT. |br|  
        Returns:
           TransactionXMLParser. Will populated using XML response.   
    
        Raises:
           Exception, For all type of exceptions    
        """
        
        if serverMode == "UAT":
            domain = ConstantResources.UAT_SERVER_URL
            userName = ConstantResources.UAT_USER_ID
            password = ConstantResources.UAT_USER_PASSWORD
        else:
            domain = ConstantResources.PRODUCTION_SERVER_URL
            userName = ConstantResources.PRODUCTION_USER_ID
            password = ConstantResources.PRODUCTION_USER_PASSWORD
            
        paramStr = {
                    "UserName" : userName,
                    "Password" : password,
                    "TransType" : transType,
                    "CheckNum" : checkNum,
                    "TransitNum" : transitNum,
                    "AccountNum" : accountNum,
                    "InvNum" : invNum,
                    "Amount" : amount,
                    "InvNum" : invNum,
                    "MICR" : micr,
                    "NameOnCheck" : nameOnCheck,
                    "DL" : dl,
                    "SS" : ss,
                    "DOB" : dob,
                    "StateCode" : stateCode,
                    "CheckType" : checkType,
                    "PNRef" : pnref,
                    "MagData" : magdata,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ProcessCheck')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            transactionXMLParser = TransactionXMLParser(response);
            return transactionXMLParser;
        else:
            return None