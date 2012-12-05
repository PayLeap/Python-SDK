'''
Created on Oct 23, 2012

'''
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.TransactionXMLParser import TransactionXMLParser
from com.payleap.constants.Constants import ConstantResources

class TransactionCardValidation:
    """This class will help you to perform different validations on card"""
    
    @staticmethod
    def processValidCard(cardNum, expDate, serverMode):   
        r"""The ValidCard service operation performs a validation check on a credit card. It checks the card length based on the card type, performs a mod 10 checksum, and checks the expiration date.   

        Args:    
            cardNum (str): The credit card number to verify. |br| 
            expDate (str): The expiration date of the credit card to verify in MMYY format. |br| 
            serverMode (str): Valid values are: PRODUCTION, UAT. |br| 
        Returns:
           TransactionXMLParser. Will populated using XML response.   
    
        Raises:
           Exception, For all type of exceptions    
        """
        
        if serverMode == "UAT":
            domain = ConstantResources.UAT_SERVER_URL
        else:
            domain = ConstantResources.PRODUCTION_SERVER_URL
            
        paramStr = {
                    "CardNumber" : cardNum,
                    "ExpDate" : expDate
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ValidCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            validationResponse = TransactionXMLParser.getValidateCardResponse(response)
            return validationResponse;
        else:
            return None   
        
    @staticmethod
    def processValidCardLength(cardNum, serverMode):   
        r"""The ValidCardLength service checks the card length based on the card type.   

        Args:    
            cardNum (str): The credit card number to verify. |br| 
            serverMode (str): Valid values are: PRODUCTION, UAT. |br| 
        Returns:
           TransactionXMLParser. Will populated using XML response.   
    
        Raises:
           Exception, For all type of exceptions    
        """
        
        if serverMode == "UAT":
            domain = ConstantResources.UAT_SERVER_URL
        else:
            domain = ConstantResources.PRODUCTION_SERVER_URL
            
        paramStr = {
                    "CardNumber" : cardNum
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ValidCardLength')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            validationResponse = TransactionXMLParser.getValidateCardLengthResponse(response)
            return validationResponse;
        else:
            return None
        
    @staticmethod
    def processValidExpDate(expDate, serverMode):   
        r"""The ValidExpDate service checks the expiration date to ensure it is valid.   

        Args:    
            expDate (str): The expiration date of the credit card to verify in MMYY format. |br| 
            serverMode (str): Valid values are: PRODUCTION, UAT. |br| 
        Returns:
           TransactionXMLParser. Will populated using XML response.   
    
        Raises:
           Exception, For all type of exceptions    
        """

        if serverMode == "UAT":
            domain = ConstantResources.UAT_SERVER_URL
        else:
            domain = ConstantResources.PRODUCTION_SERVER_URL
            
        paramStr = {
                    "ExpDate" : expDate
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ValidExpDate')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            validationResponse = TransactionXMLParser.getValidateExpDateResponse(response)
            return validationResponse;
        else:
            return None  
        
    @staticmethod
    def processValidMod10(cardNum, serverMode):   
        r"""The ValidMod10 service performs a mod 10 checksum on the card number.   

        Args:    
            cardNum (str): The credit card number to verify. |br| 
            serverMode (str): Valid values are: PRODUCTION, UAT. |br| 
        Returns:
           TransactionXMLParser. Will populated using XML response.   
    
        Raises:
           Exception, For all type of exceptions    
        """
        
        if serverMode == "UAT":
            domain = ConstantResources.UAT_SERVER_URL
        else:
            domain = ConstantResources.PRODUCTION_SERVER_URL
            
        paramStr = {
                    "CardNumber" : cardNum
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/transactservices.svc/ValidMod10')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            validationResponse = TransactionXMLParser.getValidMod10Response(response)
            return validationResponse;
        else:
            return None              
