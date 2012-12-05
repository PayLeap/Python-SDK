'''
Created on Oct 23, 2012

'''
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.TransactionXMLParser import TransactionXMLParser
from com.payleap.constants.Constants import ConstantResources

class TransactionProcessEBTCard:
    """This class will help you to send an EBT card transaction"""
    
    @staticmethod
    def processEBTCard(transType, cardNum, expDate, nameOnCard, magData, amount, invNum, pnref, 
                pin, sureChargeAmt, cashBackAmt, registerNum, extData, serverMode):   
        r"""This method will help to build the ProcessEBTCard request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed. |br| 
            cardNum (str): The EBT card number used for the transaction. |br| 
            expDate (str): The expiration date of the EBT card used for the transaction in MMYY format. |br| 
            nameOnCard (str): The cardholder's name as printed on the card. |br| 
            magData (str): The complete raw magnetic stripe data from the card wrapped in single quotes. |br| 
            amount (str): The dollar amount of the transaction in DDDDDDDDDD.CC format. This amount includes any surcharge. |br| 
            invNum (str): The invoice number used by the merchant to identify the transaction. |br| 
            pnref (str): The PNRef number. If applicable. |br| 
            pin (str): The encrypted PIN block returned by the PIN pad. The transaction will fail if an unencrypted PIN value is used. |br| 
            sureChargeAmt (str): The amount in DDDD.CC format that a merchant charges for processing a debit card transaction. |br| 
            cashBackAmt (str): The amount in DDDD.CC format that a cardholder requests for cash back. If applicable |br| 
            registerNum (str):  |br| 
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
                    "CardNum" : cardNum,
                    "ExpDate" : expDate,
                    "MagData" : magData,
                    "NameOnCard" : nameOnCard,
                    "Amount" : amount,
                    "InvNum" : invNum,
                    "PNRef" : pnref,
                    "Pin" : pin,
                    "SureChargeAmt" : sureChargeAmt,
                    "CashBackAmt" : cashBackAmt,
                    "RegisterNum" : registerNum,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ProcessEBTCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            transactionXMLParser = TransactionXMLParser(response);
            return transactionXMLParser;
        else:
            return None            
                    
       

