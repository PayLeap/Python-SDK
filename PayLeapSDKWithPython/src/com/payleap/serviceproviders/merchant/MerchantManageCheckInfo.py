'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantManageCheckInfo:
    """This class will process the ManageCheckInfo request to add, update, and delete check payment information"""
    
    @staticmethod
    def manageCheckInfo(transType, vendor, customerKey, checkInfoKey, checkType, accountType, checkNum, mICR, accountNum, transitNum, sS, dOB, 
                branchCity, dL, stateCode, nameOnCheck, email, dayPhone, street1, street2, street3, city, stateID, province, postalCode, 
                countryID, extData, serverMode):
        
        r"""This method will help to build the ManageCheckInfo request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:             
            transType (str): The transaction type being performed. Valid values are: |br| 
            Add |br| 
            Update |br| 
            Delete |br| 
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            customerKey (str): Unique numerical identifier for the customer. Found in the response values of operations for managing customer information and adding recurring payments. |br| 
            checkInfoKey (str): Unique numerical identifier for check. Found in the response values for AddRecurringCheck. |br| 
            checkType (str): Indicates check type. Valid values are: |br| 
            Personal |br| 
            Business |br| 
            accountType (str): Indicates to which type of account the check points. Valid values are: |br| 
            Checking |br| 
            Savings |br| 
            checkNum (str): The check number printed on the check. |br| 
            mICR (str): The scanned MICR data of the check. |br| 
            accountNum (str): The account number printed on the check. |br| 
            transitNum (str): The routing number printed on the check. |br| 
            sS (str): The customer's Social Security Number in ###-###-#### format. |br| 
            dOB  (str): The customer's date of birth in MM/DD/YYYY format. |br| 
            branchCity (str): The city in which the branch of the bank is located. |br| 
            dL (str): The customer's date of birth in MM/DD/YYYY format. |br| 
            stateCode (str): The customer's two-digit driver's license state or province code. |br| 
            nameOnCheck (str): The customer's name as printed on the check. |br| 
            email (str): Customer's billing email address. |br| 
            dayPhone (str): Customer's phone number in ###-###-#### format. |br| 
            street1 (str): Line 1 of customer's street address. |br| 
            street2 (str): Line 2 of customer's street address. |br| 
            street3 (str): Line 3 of customer's street address. |br| 
            city (str): Customer's city. |br| 
            stateID (str): Customer's 2-digit state code. |br| 
            province (str): Customer's province if outside the USA. |br| 
            postalCode  (str): Customer's ZIP or postal code. |br| 
            countryID (str): Customer's 3-digit country code. For example: USA, CAN. |br| 
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
                    "CheckInfoKey" : checkInfoKey,
                    "CheckType" : checkType,
                    "AccountType" : accountType,
                    "CheckNum" : checkNum,
                    "MICR" : mICR,
                    "AccountNum" : accountNum, 
                    "TransitNum" : transitNum,
                    "SS" : sS,
                    "DOB" : dOB,
                    "BranchCity" : branchCity, 
                    "DL" : dL,
                    "StateCode" : stateCode, 
                    "NameOnCheck" : nameOnCheck,
                    "Email" : email,
                    "DayPhone" : dayPhone,
                    "Street1" : street1,
                    "Street2" : street2,
                    "Street3" : street3,
                    "City" : city,
                    "StateID" : stateID,
                    "Province" : province,
                    "PostalCode" : postalCode,
                    "CountryID" : countryID,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/ManageCheckInfo')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
