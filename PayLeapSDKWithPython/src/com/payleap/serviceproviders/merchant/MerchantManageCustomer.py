'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantManageCustomer:
    """This class will processes ManageCustomer service which will allows you to add, update, and delete customer information"""
    
    @staticmethod
    def manageCustomer(transType, vendor, customerKey, customerID, customerName, firstName, lastName, title, department, street1, street2, 
                street3, city, stateID, province, zipCode, countryID, dayPhone, nightPhone, fax, email, mobile, status, extData, serverMode):
        r"""This method will help to build the ManageCustomer request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed. Valid values are: |br| 
            Add |br| 
            Update |br| 
            Delete |br| 
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            customerKey (str): Unique numerical identifier for a customer. Found in the response values for ManageCustomer, AddRecurringCreditCard, and AddRecurringCheck. |br| 
            customerID (str): Unique, merchant-supplied identifier for a customer. |br| 
            customerName (str): Customer's name. |br| 
            firstName (str): Customer's first name. |br| 
            lastName (str): Customer's last name. |br| 
            title (str): Customer's title. |br| 
            department (str): Customer's department. |br| 
            street1 (str): Line 1 of customer's street address. |br| 
            street2 (str): Line 2 of customer's street address.  |br| 
            street3 (str): Line 3 of customer's street address. |br| 
            city (str): Customer's city. |br| 
            stateID (str): Customer's 2-digit state code. |br| 
            province (str): Customer's province if outside the USA. |br| 
            zipCode (str): Customer's ZIP or postal code. |br| 
            countryID (str): Customer's 3-digit country code. For example: USA, CAN. |br| 
            dayPhone (str): Customer's daytime number in ###-###-#### format. |br| 
            nightPhone (str): Customer's nighttime number in ###-###-#### format. |br| 
            fax (str): Customer's fax number in ###-###-#### format. |br| 
            email (str): Customer's billing email address. |br| 
            mobile (str): Customer's mobile number in ###-###-#### format. |br| 
            status (str): Status |br| 
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
                    "CustomerID" : customerID,
                    "CustomerName" : customerName,
                    "FirstName" : firstName,
                    "LastName" : lastName,
                    "Title" : title,
                    "Department" : department,
                    "Street1" : street1,
                    "Street2" : street2,
                    "Street3" : street3,
                    "City" : city,
                    "StateID" : stateID,
                    "Province" : province,
                    "Zip" : zipCode,
                    "CountryID" : countryID,
                    "DayPhone" : dayPhone,
                    "NightPhone" : nightPhone,
                    "Fax" : fax,
                    "Email" : email,
                    "Mobile" : mobile,
                    "Status" : status,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/ManageCustomer')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
