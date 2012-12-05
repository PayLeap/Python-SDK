'''
Created on Oct 23, 2012

'''
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.TransactionXMLParser import TransactionXMLParser
from com.payleap.constants.Constants import ConstantResources

class TransactionProcessGiftCard:
    """This class will help you to send a gift card transaction"""
    
    @staticmethod
    def processGiftCard(transType, cardNum, expDate, magData, amount, invNum, pnref, extData, serverMode):   
        r"""This method will help to build the ProcessGiftCard request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed.  |br| 
            cardNum (str): The gift card number used for the transaction. |br| 
            expDate (str): The expiration date of the gift card used for the transaction in MMYY format. |br| 
            magData (str): The complete raw magnetic stripe data from the card wrapped in single quotes. |br| 
            amount (str): The dollar amount of the transaction in DDDDDDDDDD.CC format. |br| 
            invNum (str): The invoice number used by the merchant to identify the transaction. |br| 
            pnref (str): The PNRef number of the original transaction being refunded. If applicable. |br| 
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
                    "Amount" : amount,
                    "InvNum" : invNum,
                    "PNRef" : pnref,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ProcessGiftCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            transactionXMLParser = TransactionXMLParser(response);
            return transactionXMLParser;
        else:
            return None            