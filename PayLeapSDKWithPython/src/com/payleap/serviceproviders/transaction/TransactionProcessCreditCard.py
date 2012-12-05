'''
Created on Oct 23, 2012

'''
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.TransactionXMLParser import TransactionXMLParser
from com.payleap.constants.Constants import ConstantResources

class TransactionProcessCreditCard:
    """This class will help you to send a credit card transaction"""
    
    @staticmethod
    def processCreditCard(transType, cardNum, expDate, nameOnCard, magData, amount, invNum, pnref, 
                 zipCode, street, cvNumber, extData, serverMode):   
        r"""This method will help to build the ProcessCreditCard request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed. e.g. Sale, Adjustment etc. |br| 
            cardNum (str): The credit card number used for the transaction. |br| 
            expDate (str): The expiration date of the credit card used for the transaction in MMYY format. |br| 
            nameOnCard (str): The cardholder's name as printed on the card. |br| 
            magData (str): For swiped transactions, the complete raw magnetic stripe data from the card wrapped in single quotes.  |br| 
            amount (str): The dollar amount of the transaction in DDDDDDDDDD.CC format. This amount includes any tax or tip amounts specified in ExtData. |br| 
            invNum (str): The invoice number used by the merchant to identify the transaction. |br| 
            pnref (str): Not used for this transaction type. |br| 
            zipCode (str): The cardholder's billing ZIP code. Used for AVS. |br| 
            street (str): The cardholder's street address. Used for AVS. |br| 
            cvNumber (str): The 3 to 4 digit card verification number. For American Express, four digits displayed on the front of the card; for other card types, usually three digits displayed on the back of the card. |br| 
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
                    "Zip" : zipCode,
                    "Street" : street,
                    "CVNum" : cvNumber,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactServices.svc/ProcessCreditCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            transactionXMLParser = TransactionXMLParser(response);
            return transactionXMLParser;
        else:
            return None            
                    
       

