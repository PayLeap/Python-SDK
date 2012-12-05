'''
Created on Oct 26, 2012

'''
from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.MerchantServicesXMLResponseParser import MerchantServicesXMLResponseParser

class MerchantManageContract:
    """This class will processes ManageContract service which will allows you to add, update, and delete contract information"""
    
    @staticmethod
    def manageContract(transType, vendor, customerKey, contractKey, paymentInfoKey, paymentType, customerID, 
                customerName, firstName, lastName, title, department, street1, street2, street3, city, 
                stateID, province, zipCode, countryID, email, dayPhone, nightPhone, fax, mobile, contractID, 
                contractName, billAmt, taxAmt, totalAmt, startDate, endDate, nextBillDt, billingPeriod, 
                billingInterval, maxFailures, failureInterval, emailCustomer, emailMerchant, 
                emailCustomerFailure, emailMerchantFailure, status, extData, serverMode):
        r"""This method will help to build the ManageContract request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:             
            transType (str): The transaction type being performed. Valid values are: |br| 
            Add |br| 
            Update |br| 
            Delete |br| 
            vendor (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            customerKey (str): Unique numerical identifier for a customer. Found in the response values for ManageCustomer, AddRecurringCreditCard, and AddRecurringCheck. |br| 
            contractKey (str): Unique numerical identifier for the contract. Found in the response values for AddRecurringCheck and AddRecurringCreditCard. |br| 
            paymentInfoKey (str): Dependent on payment type. For credit cards, use a CcInfoKey or CardInfoKey. For checks, use a CheckInfoKey. |br| 
            These keys can be found in the response values of AddRecurringCreditCard, ManageCreditCardInfo, AddRecurringCheck, and ManageCheckInfo. |br| 
            paymentType (str): Indicates method of payment. Valid values are: |br| 
            CC (for credit card) |br| 
            CK (for check) |br| 
            customerID (str): Unique, merchant supplied identifier for a customer. |br| 
            customerName (str): Customer's name. |br| 
            firstName (str): Customer's first name. |br| 
            lastName (str): Customer's last name. |br| 
            title (str): Customer's title. |br| 
            department (str): Customer's department. |br| 
            street1 (str): Line 1 of customer's street address. |br| 
            street2 (str): Line 2 of customer's street address. |br| 
            street3 (str): Line 3 of customer's street address. |br| 
            city (str): Customer's city. |br| 
            stateID (str): Customer's 2 digit state code. |br| 
            province (str): Customer's province if outside the USA. |br| 
            zipCode (str): Customer's ZIP or postal code. |br| 
            countryID (str): Customer's 3 digit country code. For example: USA, CAN. |br| 
            email (str): Customer's billing email address. |br| 
            dayPhone (str): Customer's daytime number in ###-###-#### format. |br| 
            nightPhone (str): Customer's nighttime number in ###-###-#### format. |br| 
            fax (str): Customer's fax number in ###-###-#### format. |br| 
            mobile (str): Customer's mobile number in ###-###-#### format. |br| 
            contractID (str): Unique, merchant supplied identifier for the contract. |br| 
            contractName (str): Unique, merchant supplied contract name. |br| 
            billAmt (str): The amount to be billed in relation to the contract in DDDDDDDDDD.CC format. |br| 
            taxAmt (str): The tax amount in DDDD.CC format. |br| 
            totalAmt (str): The total amount of the transaction in DDDDDDDDDD.CC format. This includes any tax specified in TaxAmt. |br| 
            startDate (str): Start date of the contract in MM/DD/YYYY format. |br| 
            endDate (str): End date of the contract in MM/DD/YYYY format. If this date is not given, the contract will continue to run until manually cancelled or suspended by the system due to failure of payment. |br| 
            nextBillDt (str): Next billing date in MM/DD/YYYY format. For example: if the next billing date is scheduled to be 01/30/2015, but NextBillDt=02/15/2015 when the request is submitted, the next billing date will change to 02/15/2015. |br| 
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
            status (str): The status of the contract. Valid values include: |br| 
            Active |br| 
            Inactive |br| 
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
                    "ContractKey" : contractKey,
                    "PaymentInfoKey" : paymentInfoKey,
                    "PaymentType" : paymentType,
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
                    "DayPhone" : dayPhone,
                    "NightPhone" : nightPhone,
                    "Fax" : fax,
                    "Mobile" : mobile,
                    "ContractID" : contractID,
                    "ContractName" : contractName,
                    "BillAmt" : billAmt,
                    "TaxAmt" : taxAmt,
                    "TotalAmt" : totalAmt,
                    "StartDate" : startDate,
                    "EndDate" : endDate,
                    "NextBillDt" : nextBillDt,
                    "BillingPeriod" : billingPeriod,
                    "BillingInterval" : billingInterval,
                    "MaxFailures" : maxFailures,
                    "FailureInterval" : failureInterval,
                    "EmailCustomer" : emailCustomer,
                    "EmailMerchant" : emailMerchant,
                    "EmailCustomerFailure" : emailCustomerFailure,
                    "EmailMerchantFailure" : emailMerchantFailure,
                    "Status" : status,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/MerchantServices.svc/ManageContract')
        
        if isinstance(response, Exception):
            return response
        elif response is not None:
            merchantServiceResponse = MerchantServicesXMLResponseParser(response)
            return merchantServiceResponse;
        else:
            return None
