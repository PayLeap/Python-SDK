'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantManageCreditCardInfo:
    """This class will processes ManageCreditCardInfo service which will allows you to add allows you to add, update, and delete credit card payment information"""
    
    @staticmethod
    def manageCreditCardInfo(transType, vendor, customerKey, cardInfoKey, ccAccountNum, ccExpDate, ccNameonCard, 
                ccStreet, ccZip, extData, serverMode):
        
        r"""This method will help to build the ManageCreditCardInfo request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:             
            transType (str): The transaction type being performed. Valid values are: |br| 
            Add |br| 
            Update |br| 
            Delete |br| 
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            customerKey (str): Unique numerical identifier for a customer. Found in the response values of operations for managing customer information and adding recurring payments. |br| 
            cardInfoKey (str): Unique numerical identifier for credit card. Found in the response values for AddRecurringCreditCard as the CcInfoKey. |br| 
            ccAccountNum (str): Credit card number used for the transaction. |br| 
            ccExpDate (str): Expiration date of the credit card used for the transaction in MMYY format. |br| 
            ccNameonCard  (str): Cardholder's name as printed on the card. |br| 
            ccStreet (str): Cardholder's street address. Used for AVS. |br| 
            ccZip (str): Cardholder's billing ZIP or postal code. Used for AVS. |br| 
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
                    "TransType" : transType,
                    "Vendor" : vendor,
                    "CustomerKey" : customerKey,
                    "CardInfoKey" : cardInfoKey,
                    "CcAccountNum" : ccAccountNum,
                    "CcExpDate" : ccExpDate,
                    "CcNameonCard" : ccNameonCard,
                    "CcStreet" : ccStreet,
                    "CcZip" : ccZip,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/ManageCreditCardInfo')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
