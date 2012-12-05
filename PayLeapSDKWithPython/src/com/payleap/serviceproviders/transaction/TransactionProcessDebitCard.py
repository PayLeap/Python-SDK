'''
Created on Oct 25, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.TransactionXMLParser import TransactionXMLParser

class TransactionProcessDebitCard:
    """This class will help you to send a debit card transaction"""
    
    @staticmethod
    def processDebitCard(transType, cardNum, expDate, magData, nameOnCard, amount, invNum, pNRef, 
                 pin, sureChargeAmt, cashBackAmt, registerNum, extData, serverMode):   
        r"""This method will help to build the ProcessDebitCard request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed. |br| 
            cardNum (str): The debit card number used for the transaction. |br| 
            expDate (str): The expiration date of the debit card used for the transaction in MMYY format. |br| 
            magData (str): The complete raw magnetic stripe data from the card wrapped in single quotes. |br| 
            nameOnCard (str): The cardholder's name as printed on the card. |br| 
            amount (str): The dollar amount of the transaction in DDDDDDDDDD.CC format. This amount includes any cash back or surcharge amounts and any tax or tip amounts specified in ExtData. |br| 
            invNum (str): The invoice number used by the merchant to identify the transaction. |br| 
            pNRef (str): The PNRef number of the original sale transaction being refunded. |br| 
            pin (str): The encrypted PIN block returned by the PIN pad. The transaction will fail if an unencrypted PIN value is used. |br| 
            sureChargeAmt (str): The amount in DDDD.CC format that a merchant charges for processing a debit card transaction. |br| 
            cashBackAmt (str): The amount in DDDD.CC format that a cardholder requests for cash back |br| 
            registerNum (str): Not used |br| 
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
                    "PNRef" : pNRef,
                    "Pin" : pin,
                    "SureChargeAmt" : sureChargeAmt,
                    "CashBackAmt" : cashBackAmt,
                    "RegisterNum" : registerNum,
                    "ExtData" : extData       
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ProcessDebitCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            transactionXMLParser = TransactionXMLParser(response);
            return transactionXMLParser;
        else:
            return None