'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantAddRecurringCreditCard:
    """This class will process the AddRecurringCreditCard request to add a customer, contract, and credit card payment method all in one call"""
    @staticmethod
    def addRecurringCreditCard(vendor, customerID, customerName, firstName, lastName, title, department, 
                street1, street2, street3, city, stateID, province, zipCode, countryID, email, 
                mobile, contractID, contractName, billAmt, taxAmt, totalAmt, startDate, endDate, 
                billingPeriod, billingInterval, maxFailures, failureInterval, emailCustomer, 
                emailMerchant, emailCustomerFailure, emailMerchantFailure, ccAccountNum, ccExpdate, 
                ccNameOnCard, ccStreet, ccZip, extData, serverMode):
        
        r"""This method will help to build the AddRecurringCreditCard request, to send the same request and after getting it\'s response will extract it\'s data and will return the response   

        Args: 
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            customerID (str): Unique, merchant-supplied identifier for a customer. |br| 
            customerName (str): Name used to refer to customer in SCM API. |br| 
            firstName (str): Customer's first name. |br| 
            lastName (str): Customer's last name. |br| 
            title (str): Customer's title. |br| 
            department (str): Customer's department. |br| 
            street1 (str): Line 1 of customer's street address. |br| 
            street2 (str): Line 2 of customer's street address. |br| 
            street3 (str): Line 3 of customer's street address. |br| 
            city (str): Customer's city. |br| 
            stateID (str): Customer's 2-digit state code. |br| 
            province (str): Customer's province if outside the USA. |br| 
            zipCode (str): Customer's ZIP or postal code. |br| 
            countryID (str): Customer's 3-digit country code. For example: USA, CAN. |br| 
            email (str): Customer's billing email address. |br| 
            mobile (str): Customer's phone number in ###-###-#### format. |br| 
            contractID (str): Unique, merchant-supplied identifier for the contract. |br| 
            contractName (str): Merchant-supplied contract name. |br| 
            billAmt (str): The amount to be billed in relation to the contract in DDDDDDDDDD.CC format. |br| 
            taxAmt (str): The tax amount in DDDD.CC format. |br| 
            totalAmt (str): The total amount of the transaction in DDDDDDDDDD.CC format. This includes any tax specified in TaxAmt. |br| 
            startDate (str): Start date of the contract in MM/DD/YYYY format. |br| 
            endDate (str): End date of the contract in MM/DD/YYYY format. If this date is not given, the contract will continue to run until manually cancelled or suspended by the system due to failure of payment. |br| 
            billingPeriod (str): Used in conjunction with BillingInterval to compute next bill date. Valid values are: |br| 
            Day or Daily |br| 
            Week or Weekly |br| 
            Biweekly |br| 
            Month or Monthly |br| 
            Semimonth or Semimonthly |br| 
            Year or Annually |br| 
            Semiannually |br| 
            Quarterly |br| 
            billingInterval (str): Indicates the day on which the billing interval will be applied. |br| 
            For a BillingPeriod of Week/Weekly or Biweekly, valid values are: |br| 
            Mon or 1 |br| 
            Tue or 2 |br| 
            Wed or 3 |br| 
            Thu or 4 |br| 
            Fri or 5 |br| 
            Sat or 6 |br| 
            Sun or 7 |br| 
            For a BillingPeriod of Month/Monthly, valid values are: |br| 
            1 to 31 (the date of the month) |br| 
            Last (the last day of each month) |br| 
            For a BillingPeriod of Day/Daily, Year/Annually, Semiannually, Semimonth/Semimonthly, or Quarterly, set this parameter to 0. The system will calculate the BillingInterval using the StartDate in the contract. |br| 
            maxFailures (str): The maximum number of attempts to submit a payment before system puts contract into a suspended mode. |br| 
            failureInterval (str): The number of days system will wait between each reattempt at processing payment. |br| 
            emailCustomer (str): Indicates whether to email the customer regarding the status of recurring payment. Valid values are: True or False. |br| 
            emailMerchant (str): Indicates whether to email the merchant regarding the status of recurring payment. Valid values are: True or False. |br| 
            emailCustomerFailure (str): Indicates whether to email the customer if recurring payment fails. Valid values are: True or False. |br| 
            emailMerchantFailure (str): Indicates whether to email the merchant if recurring payment fails. Valid values are: True or False. |br| 
            ccAccountNum (str): Credit card number used for the transaction. |br| 
            ccExpdate (str): Expiration date of the credit card used for the transaction in MMYY format. |br| 
            ccNameOnCard (str): Cardholder's name as printed on the card. |br| 
            ccStreet (str): Cardholder's street Address. Used for AVS. |br| 
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
                    "Vendor" : vendor,
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
                    "Email" : email,
                    "Mobile" : mobile,
                    "ContractID" : contractID,
                    "ContractName" : contractName,
                    "BillAmt" : billAmt,
                    "TaxAmt" : taxAmt,
                    "TotalAmt" : totalAmt,
                    "StartDate" : startDate,
                    "EndDate" : endDate,
                    "BillingPeriod" : billingPeriod,
                    "BillingInterval" : billingInterval,
                    "MaxFailures" : maxFailures,
                    "FailureInterval" : failureInterval,
                    "EmailCustomer" : emailCustomer,
                    "EmailMerchant" : emailMerchant,
                    "EmailCustomerFailure" : emailCustomerFailure,
                    "EmailMerchantFailure" : emailMerchantFailure,
                    "CcAccountNum" : ccAccountNum,
                    "CcExpdate" : ccExpdate,
                    "CcNameOnCard" : ccNameOnCard,
                    "CcStreet" : ccStreet,
                    "CcZip" : ccZip,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/AddRecurringCreditCard')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
