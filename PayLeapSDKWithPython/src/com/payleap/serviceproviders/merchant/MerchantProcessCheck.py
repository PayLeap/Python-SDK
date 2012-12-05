'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantProcessCheck:
    """This class will processes check transactions within the recurring billing module"""
    
    @staticmethod
    def processCheck(vendor, checkInfoKey, amount, invNum, extData, serverMode):
        r"""This method will help to build the ProcessCheck request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:             
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            checkInfoKey (str): Unique numerical identifier for check. Found in the response values for AddRecurringCheck and ManageCheckInfo. |br| 
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
                    "CheckInfoKey" : checkInfoKey,
                    "Amount" : amount,
                    "InvNum" : invNum,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/ProcessCheck')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
