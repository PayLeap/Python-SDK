'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantProcessCreditCard:
    """This class will process the ProcessCreditCard request which will processes credit card transactions within the recurring billing module"""
    
    @staticmethod
    def processCreditCard(vendor, ccInfoKey, amount, invNum, extData, serverMode):
        r"""This method will help to build the ProcessCreditCard request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:             
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            ccInfoKey (str): Unique numerical identifier for credit card. Found in the response values for AddRecurringCreditCard and ManageCreditCardInfo. |br| 
            amount (str): The dollar amount of the transaction in DDDDDDDDDD.CC format. |br| 
            invNum (str): The invoice number used by the merchant to identify the transaction. |br| 
            extData (str): Not used for this operation. |br| 
            serverMode (str): Valid values are: PRODUCTION, UAT. |br| 
        Returns:
           MerchantServicesXMLResponseParser. Will populated using XML response.   
    
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
                    "Username" : userName,
                    "Password" : password,
                    "Vendor" : vendor,
                    "CcInfoKey" : ccInfoKey,
                    "Amount" : amount,
                    "InvNum" : invNum,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/ProcessCreditCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
