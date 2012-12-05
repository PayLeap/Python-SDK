'''
Created on Oct 23, 2012

'''


import wx
from com.payleap.serviceproviders.transaction.TransactionProcessCreditCard import TransactionProcessCreditCard
from com.payleap.serviceproviders.merchant.MerchantProcessCreditCard import MerchantProcessCreditCard

class TestApplication:
    
    if __name__ == '__main__':
        
        #***************************************************** Transaction Services ********************************************
        
        #Sample ProcessCreditCard request
        #https://uat.payleap.com/transactservices.svc/ProcessCreditCard?UserName=user123_API&Password=Nn2jCtsOuxVlcELE&TransType=Sale&CardNum=4111111111111111&ExpDate=1212&MagData=&NameOnCard=JohnDoe&Amount=1&InvNum=&PNRef=&Zip=98375&Street=&CVNum=&ExtData=
        #=======================================================================
        # transactionXMLParser = ProcessCreditCardSP.process(
        #                            "Sale", #TransType
        #                            "4111111111111111", #CardNum
        #                            "1215", #ExpDate
        #                            "Name Python", #NameOnCard
        #                            "", #MagData
        #                            "1", #Amount
        #                            "", #InvNum
        #                            "", #PNRef
        #                            "98375", #Zip
        #                            "", #Street
        #                            "", #CVNumber
        #                            "", #ExtData
        #                            "UAT" #ServerMode                                  
        #                            )  
        # if transactionXMLParser is not None:
        #    print "Response : ", transactionXMLParser.respMSG , ", Response Code: " , transactionXMLParser.result , ", Response Msg: ", transactionXMLParser.message , ", PNRef: ", transactionXMLParser.PNRef , ", AuthCode: ", transactionXMLParser.authCode , ", Token Number: ", transactionXMLParser.tokenNumber
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Sample ProcessCheck request (Check sale transaction request)          
        #https://uat.payleap.com/transactservices.svc/ProcessCheck?UserName=user123_API&Password=Ew3Kg6cV9MD9Ja@v&TransType=Sale&CheckNum=1234&TransitNum=262084356&AccountNum=1234567890&InvNum=&Amount=1.00&MICR=&NameOnCheck=John%20Doe&DL=&SS=&DOB=&StateCode=WA&CheckType=Personal&PNRef=&MagData=&ExtData=%3CSecCode%3EWEB%3C/SecCode%3E    
        #=======================================================================
        # transactionXMLParser = ProcessCheckSP.process(
        #                            "Sale", #TransType
        #                            "1234", #CheckNum
        #                            "262084356", #TransitNum
        #                            "1234567890", #AccountNum
        #                            "", #InvNum
        #                            "1.00", #Amount
        #                            "", #MICR
        #                            "Name", #NameOnCheck
        #                            "", #DL
        #                            "", #SS
        #                            "", #DOB
        #                            "WA", #StateCode 
        #                            "Personal", #CheckType
        #                            "", #PNRef
        #                            "", #MagData
        #                            "<SecCode>WEB</SecCode>", #ExtData
        #                            "UAT" #ServerMode
        #                            )
        # if transactionXMLParser is not None:
        #    print "Response : ", transactionXMLParser.respMSG , ", Response Code: " , transactionXMLParser.result , ", Response Msg: ", transactionXMLParser.message , ", PNRef: ", transactionXMLParser.PNRef , ", AuthCode: ", transactionXMLParser.authCode , ", Token Number: ", transactionXMLParser.tokenNumber
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a debit card sale transaction request
        #https://uat.payleap.com/transactservices.svc/ProcessDebitCard?UserName=user123_API&Password=Ew3Kg6cV9MD9Ja@v&TransType=Sale&CardNum=4111111111111111&ExpDate=1215&MagData=4055011111111111=05121015432112345678&NameOnCard=&Amount=18.1&InvNum=&PNRef=&Pin=1234&SureChargeAmt=&CashBackAmt=&RegisterNum=&ExtData=%3CKeySerialNumber%3E4A003102930003BB%3C%2FKeySerialNumber%3E
        #=======================================================================
        # transactionXMLParser = ProcessDebitCard.process(
        #                            "Sale", #TransType
        #                            "4111111111111111", #CardNum
        #                            "1215", #ExpDate
        #                            "4055011111111111=05121015432112345678", #MagData
        #                            "", #NameOnCard
        #                            "18.2", #Amount
        #                            "", #InvNum
        #                            "", #PNRef
        #                            "1234", #Pin
        #                            "", #SureChargeAmt
        #                            "", #CashBackAmt
        #                            "", #RegisterNum
        #                            "<KeySerialNumber>4A003102930003BB</KeySerialNumber>", #ExtData
        #                            "UAT" #ServerMode
        #                            )
        # 
        # if transactionXMLParser is not None:
        #    print "Response : ", transactionXMLParser.respMSG , ", Response Code: " , transactionXMLParser.result , ", Response Msg: ", transactionXMLParser.message , ", PNRef: ", transactionXMLParser.PNRef , ", AuthCode: ", transactionXMLParser.authCode , ", Token Number: ", transactionXMLParser.tokenNumber
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of an EBT food stamp sale transaction request
        #https://uat.payleap.com/transactservices.svc/ProcessEBTCard?UserName=user123_API&Password=Ew3Kg6cV9MD9Ja@v&TransType=FoodStampSale&CardNum=4111111111111111&ExpDate=1215&MagData=4111111111111111=05121015432112345678&NameOnCard=&Amount=10.13&InvNum=1&PNRef=&Pin=1234&SureChargeAmt=&CashBackAmt=&RegisterNum=&ExtData=%3CKeySerialNumber%3E4A003102930003BB%3C%2FKeySerialNumber%3E
        #=======================================================================
        # transactionXMLParser = ProcessEBTCard.process(
        #                    "FoodStampSale", #TransType
        #                    "4111111111111111", #CardNum
        #                    "1215", #ExpDate
        #                    "4055011111111111=05121015432112345678", #MagData
        #                    "", #NameOnCard
        #                    "10.14", #Amount
        #                    "", #InvNum
        #                    "", #PNRef
        #                    "1234", #Pin
        #                    "", #SureChargeAmt
        #                    "", #CashBackAmt
        #                    "", #RegisterNum
        #                    "<KeySerialNumber>4A003102930003BB</KeySerialNumber>", #ExtData
        #                    "UAT" #ServerMode
        #            )
        # 
        # if transactionXMLParser is not None:
        #    print "Response : ", transactionXMLParser.respMSG , ", Response Code: " , transactionXMLParser.result , ", Response Msg: ", transactionXMLParser.message , ", PNRef: ", transactionXMLParser.PNRef , ", AuthCode: ", transactionXMLParser.authCode , ", Token Number: ", transactionXMLParser.tokenNumber
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of gift card redeem transaction request
        #https://uat.payleap.com/transactservices.svc/ProcessGiftCard?UserName=user123_API&Password=Ew3Kg6cV9MD9Ja@v&TransType=Redeem&CardNum=4111111111111111&ExpDate=1215&MagData=&Amount=1&InvNum=&PNRef=&ExtData=        
        #=======================================================================
        # transactionXMLParser = ProcessGiftCardSP.process(
        #            "Redeem", #TransType
        #            "4111111111111111", #CardNum
        #            "1215", #ExpDate
        #            "", #MagData
        #            "1", #Amount
        #            "", #InvNum
        #            "", #PNRef
        #            "", #ExtData
        #            "UAT" #ServerMode
        #    )
        # 
        # if transactionXMLParser is not None:
        #    print "Response : ", transactionXMLParser.respMSG , ", Response Code: " , transactionXMLParser.result , ", Response Msg: ", transactionXMLParser.message , ", PNRef: ", transactionXMLParser.PNRef , ", AuthCode: ", transactionXMLParser.authCode , ", Token Number: ", transactionXMLParser.tokenNumber
        # else:
        #    print "Empty response"
        #=======================================================================
       
        #Example of a card validation request
        #https://uat.payleap.com/transactservices.svc/ValidCard?CardNumber=4111111111111111&ExpDate=1215 
        #=======================================================================
        # validationResponse = ValidationSP.processValidCard(
        #            "4012888888881881", #CardNum
        #            "1215", #ExpDate
        #            "UAT" #ServerMode
        #    )
        # 
        # if validationResponse is not None:
        #    print "Response : ", validationResponse
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a card length validation request
        #https://uat.payleap.com/transactservices.svc/ValidCardLength?CardNumber=4111111111111111 
        #=======================================================================
        # validationResponse = ValidationSP.processValidCardLength(
        #            "4012888888881881", #CardNum
        #            "UAT" #ServerMode
        #    )
        # 
        # if validationResponse is not None:
        #    print "Response : ", validationResponse
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of an expiration date validation request
        #https://uat.payleap.com/transactservices.svc/ValidExpDate?ExpDate=1215 
        #=======================================================================
        # validationResponse = ValidationSP.processValidExpDate(
        #            "1111", #ExpDate
        #            "UAT" #ServerMode
        #    )
        # 
        # if validationResponse is not None:
        #    print "Response : ", validationResponse
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a mod 10 check
        #https://uat.payleap.com/transactservices.svc/ValidMod10?CardNumber=4111111111111111 
        #=======================================================================
        # validationResponse = ValidationSP.processValidMod10(
        #            "401288888888188", #CardNum
        #            "UAT" #ServerMode
        #    )
        # 
        # if validationResponse is not None:
        #    print "Response : ", validationResponse
        # else:
        #    print "Empty response"
        #=======================================================================
        
        
        
        #***************************************************** Merchant Services ********************************************
        
        #Example of an AddRecurringCreditCard request
        #https://uat.payleap.com/MerchantServices.svc/AddRecurringCreditCard?Username=user123_API&Password=Nn2jCtsOuxVlcELE&Vendor=123&CustomerID=12345&CustomerName=ABCompany&FirstName=John&LastName=Doe&Title=&Department=&Street1=&Street2=&Street3=&City=&StateID=&Province=&Zip=&CountryID=&Email=&Mobile=&ContractID=i&ContractName=ABCService&BillAmt=45.00&TaxAmt=&TotalAmt=4500&StartDate=01/01/2012&EndDate=&BillingPeriod=Week&BillingInterval=1&MaxFailures=&FailureInterval=&EmailCustomer=&EmailMerchant=&EmailCustomerFailure=&EmailMerchantFailure=&CcAccountNum=1234567890987654&CcExpdate=1212&CcNameOnCard=&CcStreet=&CcZip=&ExtData=
        #=======================================================================
        # merchantServiceResponse = AddRecurringCreditCardSP.process(
        #            "415",  #Vendor              
        #            "12345",  #CustomerID          
        #            "ABCompany",  #CustomerName        
        #            "John",  #FirstName           
        #            "Doe",  #LastName            
        #            "",  #Title               
        #            "",  #Department          
        #            "",  #Street1             
        #            "",  #Street2             
        #            "",  #Street3             
        #            "",  #City                
        #            "",  #StateID             
        #            "",  #Province            
        #            "",  #Zip                 
        #            "",  #CountryID           
        #            "",  #Email               
        #            "",  #Mobile              
        #            "i",  #ContractID          
        #            "ABCService",  #ContractName        
        #            "1",  #BillAmt             
        #            "0",  #TaxAmt              
        #            "1",  #TotalAmt            
        #            "01/01/2012",  #StartDate           
        #            "",  #EndDate             
        #            "Week",  #BillingPeriod       
        #            "1",  #BillingInterval     
        #            "",  #MaxFailures         
        #            "",  #FailureInterval     
        #            "",  #EmailCustomer       
        #            "",  #EmailMerchant       
        #            "",  #EmailCustomerFailure
        #            "",  #EmailMerchantFailure
        #            "4012888888881881",  #CcAccountNum        
        #            "1212",  #CcExpdate           
        #            "",  #CcNameOnCard        
        #            "",  #CcStreet            
        #            "",  #CcZip               
        #            "",  #ExtData 
        #            "UAT" #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of an AddRecurringCheck request
        #https://uat.payleap.com/MerchantServices.svc/AddRecurringCheck?Username=user123_API&Password=Nn2jCtsOuxVlcELE&Vendor=123&CustomerID=12345&CustomerName=Gravity%20Apples&FirstName=Isaac&LastName=Newton&Title=&Department=&Street1=123%20Main%20St&Street2=&Street3=&City=Lincolnshire&StateID=GA&Province=&Zip=12345&CountryID=&Email=&Mobile=123-456-7890&ContractID=54321&ContractName=Required&BillAmt=1&TaxAmt=&TotalAmt=1&StartDate=01/09/2012&EndDate=&BillingPeriod=Month&BillingInterval=1&MaxFailures=&FailureInterval=&EmailCustomer=&EmailMerchant=&EmailCustomerFailure=&EmailMerchantFailure=&CheckType=Personal&AccountType=Checking&CheckNum=&MICR=&AccountNum=1234567890001&TransitNum=987654321&SS=&DOB=12/25/1642&BranchCity=&DL=&StateCode=&NameOnCheck=&ExtData=
        #=======================================================================
        # merchantServiceResponse = AddRecurringCheckSP.process(
        #            "415",#              Vendor              
        #            "12345",#            CustomerID          
        #            "Gravity Apples",# CustomerName        
        #            "Isaac",#            FirstName           
        #            "Newton",#           LastName            
        #            "",#                 Title               
        #            "",#                 Department          
        #            "123 Main St",#  Street1             
        #            "",#                 Street2             
        #            "",#                 Street3             
        #            "Lincolnshire",#     City                
        #            "GA",#               StateID             
        #            "",#                 Province            
        #            "12345",#            Zip                 
        #            "",#                 CountryID           
        #            "",#                 Email               
        #            "9096414117",#     Mobile              
        #            "54321",#            ContractID          
        #            "Required",#         ContractName        
        #            "1",#                BillAmt             
        #            "",#                 TaxAmt              
        #            "1",#                TotalAmt            
        #            "01/09/2012",#       StartDate           
        #            "",#                 EndDate             
        #            "Month",#            BillingPeriod       
        #            "1",#                BillingInterval     
        #            "",#                 MaxFailures         
        #            "",#                 FailureInterval     
        #            "",#                 EmailCustomer       
        #            "",#                 EmailMerchant       
        #            "",#                 EmailCustomerFailure
        #            "",#                 EmailMerchantFailure
        #            "Personal",#         CheckType           
        #            "Checking",#         AccountType         
        #            "",#                 CheckNum            
        #            "",#                 MICR                
        #            "1234567890001",#    AccountNum          
        #            "987654321",#        TransitNum          
        #            "",#                 SS                  
        #            "",#       DOB                 
        #            "",#                 BranchCity          
        #            "",#                 DL                  
        #            "",#                 StateCode           
        #            "",#                 NameOnCheck         
        #            "",#                 ExtData  
        #            "UAT" #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a ProcessCreditCard - Recurring billing request
        #https://uat.payleap.com/MerchantServices.svc/ProcessCreditCard?Username=user123_API&Password=Nn2jCtsOuxVlcELE&Vendor=123&CcInfoKey=1234&Amount=11.00&InvNum=&ExtData=
        #=======================================================================
        # merchantServiceResponse = ProcessCreditCardRecurringBillingSP.process(
        #            "415",#              Vendor 
        #            "1234",#              CcInfoKey             
        #            "1.00",#            Amount          
        #            "",#                 InvNum         
        #            "",#                 ExtData  
        #            "UAT" #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of ProcessCheck request
        #https://uat.payleap.com/MerchantServices.svc/ProcessCheck?Username=user123_API&Password=Nn2jCtsOuxVlcELE&Vendor=123&CheckInfoKey=1234&Amount=11.00&InvNum=&ExtData=
        #=======================================================================
        # merchantServiceResponse = ProcessCheckRecurringBillingSP.process(
        #            "415",#              Vendor 
        #            "",#              checkInfoKey             
        #            "1.00",#            Amount          
        #            "",#                 InvNum         
        #            "",#                 ExtData  
        #            "UAT" #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        
        #Example of a ManageCheckInfo request
        #https://uat.payleap.com/MerchantServices.svc/ManageCheckInfo?Username=user123_API&Password=Nn2jCtsOuxVlcELE&TransType=Add&Vendor=123&CustomerKey=1234&CheckInfoKey=&CheckType=Personal&AccountType=Checking&CheckNum=&MICR=&AccountNum=1234567890001&TransitNum=261072770&SS=&DOB=&BranchCity=&DL=&StateCode=&NameOnCheck=&Email=&DayPhone=&Street1=&Street2=&Street3=&City=&StateID=&Province=&PostalCode=&CountryID=&ExtData=
        #=======================================================================
        # merchantServiceResponse = ManageCheckInfoSP.process(
        #            "Add",#           TransType   
        #            "415",#           Vendor      
        #            "1234",#          CustomerKey 
        #            "",#              CheckInfoKey
        #            "Personal",#      CheckType   
        #            "Checking",#      AccountType 
        #            "",#              CheckNum    
        #            "",#              MICR        
        #            "1234567890001",# AccountNum  
        #            "261072770",#     TransitNum  
        #            "",#              SS          
        #            "",#              DOB         
        #            "",#              BranchCity  
        #            "",#              DL          
        #            "",#              StateCode   
        #            "",#              NameOnCheck 
        #            "",#              Email       
        #            "",#              DayPhone    
        #            "",#              Street1     
        #            "",#              Street2     
        #            "",#              Street3     
        #            "",#              City        
        #            "",#              StateID     
        #            "",#              Province    
        #            "",#              PostalCode  
        #            "",#              CountryID   
        #            "",#              ExtData    
        #            "UAT" #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a ManageCreditCardInfo request
        #https://uat.payleap.com/MerchantServices.svc/ManageCreditCardInfo?Username=user123_API&Password=Nn2jCtsOuxVlcELE&TransType=Add&Vendor=123&CustomerKey=6022&CardInfoKey=&CcAccountNum=8675309867530900&CcExpDate=1212&CcNameonCard=Tommy%20Tutone&CcStreet=&CcZip=&ExtData=
        #=======================================================================
        # merchantServiceResponse = ManageCreditCardInfoSP.process(
        #            "Add", #             TransType
        #            "415", #             Vendor
        #            "6022", #            CustomerKey
        #            "", #                CardInfoKey
        #            "8675309867530900", #CcAccountNum
        #            "1212", #            CcExpDate
        #            "Tommy Tutone", #    CcNameonCard
        #            "", #                CcStreet
        #            "", #                CcZip
        #            "", #                ExtData    
        #            "UAT" #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a ManageContract request
        #https://uat.payleap.com/MerchantServices.svc/ManageContract?Username=user123_API&Password=ENn2jCtsOuxVlcELE&TransType=Add&Vendor=123&CustomerKey=6022&ContractKey=&PaymentInfoKey=5452&PaymentType=CC&CustomerID=13579&CustomerName=Garfield%20&%20Friends&FirstName=Jon&LastName=Arbuckle&Title=&Department=&Street1=&Street2=&Street3=&City=&StateID=&Province=&Zip=&CountryID=&Email=&DayPhone=&NightPhone=&Fax=&Mobile=&ContractID=12346&ContractName=Lasagna&BillAmt=400.00&TaxAmt=3.00&TotalAmt=403.00&StartDate=01/11/2012&EndDate=&NextBillDt=01/11/2012&BillingPeriod=Semimonthly&BillingInterval=0&MaxFailures=&FailureInterval=&EmailCustomer=&EmailMerchant=&EmailCustomerFailure=&EmailMerchantFailure=&Status=&ExtData=
        #=======================================================================
        # merchantServiceResponse = ManageContractSP.process(
        #            "Add",         #TransType
        #            "415",         #Vendor
        #            "6102",        #CustomerKey
        #            "",            #ContractKey
        #            "5452",        #PaymentInfoKey
        #            "CC",          #PaymentType
        #            "13579",       #CustomerID
        #            "Garfield",    #CustomerName
        #            "Jon",         #FirstName
        #            "Arbuckle",    #LastName
        #            "",            #Title
        #            "",            #Department
        #            "",            #Street1
        #            "",            #Street2
        #            "",            #Street3
        #            "",            #City
        #            "",            #StateID
        #            "",            #Province
        #            "",            #Zip
        #            "",            #CountryID
        #            "",            #Email
        #            "",            #DayPhone
        #            "",            #NightPhone
        #            "",            #Fax
        #            "",            #Mobile
        #            "12346",       #ContractID
        #            "Lasagna",     #ContractName
        #            "400.00",      #BillAmt
        #            "3.00",        #TaxAmt
        #            "403.00",      #TotalAmt
        #            "01/11/2012",  #StartDate
        #            "",            #EndDate
        #            "01/11/2012",  #NextBillDt
        #            "Semimonthly", #BillingPeriod
        #            "0",           #BillingInterval
        #            "",            #MaxFailures
        #            "",            #FailureInterval
        #            "",            #EmailCustomer
        #            "",            #EmailMerchant
        #            "",            #EmailCustomerFailure
        #            "",            #EmailMerchantFailure
        #            "",            #Status
        #            "",            #ExtData
        #            "UAT"          #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.ccInfoKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        #Example of a ManageCustomer request
        #https://uat.payleap.com/MerchantServices.svc/ManageCustomer?Username=user123_API&Password=Nn2jCtsOuxVlcELE&TransType=Add&Vendor=123&CustomerKey=&CustomerID=12345&CustomerName=ComedyCo&FirstName=Jack&LastName=Black&Title=&Department=&Street1=&Street2=&Street3=&City=&StateID=&Province=&Zip=&CountryID=&DayPhone=&NightPhone=&Fax=&Email=&Mobile=&Status=&ExtData=
        #=======================================================================
        # merchantServiceResponse = ManageCustomerSP.process(
        #            "Add",#      TransType   
        #            "415",#      Vendor      
        #            "",#         CustomerKey 
        #            "",#    CustomerID  
        #            "Name D1",# CustomerName
        #            "Name",#     FirstName   
        #            "D1",#    LastName    
        #            "",#         Title       
        #            "",#         Department  
        #            "",#         Street1     
        #            "",#         Street2     
        #            "",#         Street3     
        #            "",#         City        
        #            "",#         StateID     
        #            "",#         Province    
        #            "",#         Zip         
        #            "",#         CountryID   
        #            "",#         DayPhone    
        #            "",#         NightPhone  
        #            "",#         Fax         
        #            "",#         Email       
        #            "",#         Mobile      
        #            "",#         Status      
        #            "",#         ExtData 
        #            "UAT"        #ServerMode
        #    )
        # 
        # if merchantServiceResponse is not None:
        #    print "Message : ", merchantServiceResponse.message , ", CCInfoKey: " , merchantServiceResponse.customerKey , ", CheckInfoKey: ", merchantServiceResponse.checkInfoKey , ", PNRef: ", merchantServiceResponse.pnref , ", Result: ", merchantServiceResponse.result , ", Error: ", merchantServiceResponse.error
        # else:
        #    print "Empty response"
        #=======================================================================
        
        # ************************************* Reporting Services *********************************
        #Example of a GetCardTrx request
        #https://uat.payleap.com/reportingservices.svc/GetCardTrx?UserName=user123_API&Password=test&RPNum=123&PNRef=&BeginDt=2000-01-01&EndDt=3000-01-01&PaymentType=&ExcludePaymentType=&TransType=Sale &ExcludeTransType=&ApprovalCode=&Result=&ExcludeResult=&NameOnCard=&CardNum=&CardType=&ExcludeCardType=&ExcludeVoid=TRUE&User=&InvoiceId=&SettleFlag=&SettleMsg=&SettleDt=&TransformType= &Xsl=&ColDelim=&RowDelim=&IncludeHeader=TRUE&ExtData=
        
        #=======================================================================
        # cardTrxResponse = GetCardTrxSP.process(
        #                                       "415", #       RPNum               
        #                                        "", #          PNRef                
        #                                        "2011-09-29", #BeginDt              
        #                                        "2012-10-29", #EndDt                
        #                                        "", #          PaymentType          
        #                                        "", #          ExcludePaymentType   
        #                                        "", #      TransType            
        #                                        "", #          ExcludeTransType     
        #                                        "", #          ApprovalCode         
        #                                        "", #          Result               
        #                                        "", #          ExcludeResult        
        #                                        "", #          NameOnCard           
        #                                        "", #          CardNum              
        #                                        "", #          CardType             
        #                                        "", #          ExcludeCardType      
        #                                        "", #          ExcludeVoid          
        #                                        "", #          User                 
        #                                        "", #          InvoiceId            
        #                                        "", #          SettleFlag           
        #                                        "", #          SettleMsg            
        #                                        "", #          SettleDt             
        #                                        "", #          TransformType        
        #                                        "", #          Xsl                  
        #                                        "", #          ColDelim             
        #                                        "", #          RowDelim             
        #                                        "", #          IncludeHeader        
        #                                        "", #          ExtData 
        #                                        "UAT"        #ServerMode
        #                                        )
        # if(cardTrxResponse is not None):
        #    if isinstance(cardTrxResponse, Exception):
        #        print "Error while processing your request: " , cardTrxResponse
        #    else:
        #        if isinstance(cardTrxResponse, list):
        #            print "length: " , len(cardTrxResponse)
        #            for item in cardTrxResponse:
        #                print "TRX_HD_Key: ", item.TRX_HD_Key
        #        else:
        #            #Error occured
        #            print cardTrxResponse
        # else:
        #    print "Error: Blank response found"
        #=======================================================================
        
        #Example of a GetCardTrxSummary request
        #https://uat.payleap.com/reportingservices.svc/GetCardTrxSummary?UserName=user123_API&Password=test&RPNum=123&BeginDt=2000-01-01&EndDt=3000-01-01&ApprovalCode=&Register=&NameOnCard=&CardNum=&CardType=VISA&ExcludeVoid=FALSE&User=&SettleFlag=&SettleMsg=&SettleDt=&TransformType=&Xsl=&ColDelim=&RowDelim=&IncludeHeader=&ExtData=
        #=======================================================================
        # cardTrxSummeryResp = GetCardTrxSummarySP.process(
        #                                        "415", #        RPNum        
        #                                        "2012-01-01", # BeginDt      
        #                                        "2012-10-29", # EndDt        
        #                                        "", #           ApprovalCode 
        #                                        "", #           Register     
        #                                        "", #           NameOnCard   
        #                                        "", #           CardNum      
        #                                        "", #       CardType     
        #                                        "", #           ExcludeVoid  
        #                                        "", #           User         
        #                                        "", #           SettleFlag   
        #                                        "", #           SettleMsg    
        #                                        "", #           SettleDt     
        #                                        "", #           TransformType
        #                                        "", #           Xsl          
        #                                        "", #           ColDelim     
        #                                        "", #           RowDelim     
        #                                        "", #           IncludeHeader
        #                                        "", #           ExtData       
        #                                        "UAT"        #ServerMode
        #                                        )
        # if(cardTrxSummeryResp is not None):
        #    if isinstance(cardTrxSummeryResp, Exception):
        #        print "Error while processing your request: " , cardTrxSummeryResp
        #    else:
        #        if isinstance(cardTrxSummeryResp, list):
        #            print "length: " , len(cardTrxSummeryResp)
        #            for item in cardTrxSummeryResp:
        #                print "Payment_Type_ID: ", item.Payment_Type_ID
        #        else:
        #            #Error occured
        #            print cardTrxSummeryResp
        # else:
        #    print "Error: Blank response found"
        #=======================================================================
        
        #Example of a GetCheckTrx request:
        #https://uat.payleap.com/reportingservices.svc/GetCheckTrx?UserName=user123_API&Password=test&RPNum=123&PNRef=&BeginDt=2011-09-20T12:00:00&EndDt=2011-09-20T12:30:00&PaymentType=VERIFY&ExcludePaymentType=&TransType=&ExcludeTransType=&ApprovalCode=&Result=0&ExcludeResult=&NameOnCheck=&CheckNum=&AcctNum=&RouteNum=&ExcludeVoid=&User=&InvoiceId=&SettleFlag=&SettleMsg=&SettleDt=&TransformType=&Xsl=&ColDelim=&RowDelim=&IncludeHeader=&ExtData=
        #=======================================================================
        # checkTrxResponse = GetCheckTrxSP.process(
        #                                        "415", #
        #                                        "", #
        #                                        "2011-09-20T12:00:00", #
        #                                        "2012-10-29T12:30:00", #
        #                                        "VERIFY", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "0", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #
        #                                        "", #       
        #                                        "UAT"        #ServerMode
        #                                        )
        # if(checkTrxResponse is not None):
        #    if isinstance(checkTrxResponse, Exception):
        #        print "Error while processing your request: " , checkTrxResponse
        #    else:
        #        if isinstance(checkTrxResponse, list):
        #            print "length: " , len(checkTrxResponse)
        #            for item in checkTrxResponse:
        #                print "Trx_HD_Key: ", item.Trx_HD_Key
        #        else:
        #            #Error occured
        #            print checkTrxResponse
        # else:
        #    print "Error: Blank response found"
        #=======================================================================
        
        #Example of a GetInfo request using the BatchInquiry TransType
        #https://uat.payleap.com/reportingservices.svc/GetInfo?UserName=user123_API&Password=test&TransType=BatchInquiry&ExtData=
        #=======================================================================
        # infoserviceResponse = GetInfoSP.process(
        #                                        "Setup", # TransType
        #                                        "", #   ExtData                                                   
        #                                        "UAT"        #ServerMode
        #                                        )
        # if(infoserviceResponse is not None):
        #    if isinstance(infoserviceResponse, Exception):
        #        print "Error while processing your request: " , infoserviceResponse
        #    else:
        #        if isinstance(infoserviceResponse, list):
        #            print "length: " , len(infoserviceResponse)
        #            for item in infoserviceResponse:
        #                print "RespMSG: ", item.RespMSG
        #        else:
        #            #Error occured
        #            print infoserviceResponse
        # else:
        #    print "Error: Blank response found"
        #=======================================================================
        
        #Example of a GetOpenBatchSummary request
        #https://uat.payleap.com/reportingservices.svc/GetOpenBatchSummary?UserName=user123_API&Password=test&RPNum=123&BeginDt=&EndDt=&ExtData=
        #=======================================================================
        # openBatchSummaryResponse = GetOpenBatchSummarySP.process(
        #                                        "415", # RPNum
        #                                        "", #   beginDt  
        #                                        "", # endDt
        #                                        "", #   extData                                                     
        #                                        "UAT"        #ServerMode
        #                                        )
        # if(openBatchSummaryResponse is not None):
        #    if isinstance(openBatchSummaryResponse, Exception):
        #        print "Error while processing your request: " , openBatchSummaryResponse
        #    else:
        #        if isinstance(openBatchSummaryResponse, list):
        #            print "length: " , len(openBatchSummaryResponse)
        #            for item in openBatchSummaryResponse:
        #                print "Sale: ", item.Sale
        #        else:
        #            #Error occured
        #            print openBatchSummaryResponse
        # else:
        #    print "Error: Blank response found"
        #=======================================================================
        
        #Custom token sample
        trProcessCreditCardResponse = TransactionProcessCreditCard.processCreditCard(
                                    "Sale", #TransType
                                    "4111111111111111", #CardNum
                                    "1215", #ExpDate
                                    "Name Python", #NameOnCard
                                    "", #MagData
                                    "6", #Amount
                                    "", #InvNum
                                    "", #PNRef
                                    "98375", #Zip
                                    "", #Street
                                    "", #CVNumber
                                    "<CustomerTokenization>T</CustomerTokenization>", #ExtData
                                    "UAT" #ServerMode                                  
                                    )
        
        if(trProcessCreditCardResponse is not None):
            if isinstance(trProcessCreditCardResponse, Exception):
                print "Error while processing your request: " , trProcessCreditCardResponse
            else:
                if trProcessCreditCardResponse.result == 0:
                    print "************** Custom Token Transaction Credit Response Started *********************"
                    print "Result: " , trProcessCreditCardResponse.result
                    print "Resp Message: " , trProcessCreditCardResponse.respMSG
                    print "Message 1: " , trProcessCreditCardResponse.message1
                    print "Message 2: " , trProcessCreditCardResponse.message2
                    print "Token Number: " , trProcessCreditCardResponse.tokenNumber
                    print "************** Custom Token Transaction Credit Response  Completed *********************"

                    #===========================================================
                    # Populating billing form to bill a customer using received Token number from above request
                    #===========================================================
                    
                    merchantServiceResponse = MerchantProcessCreditCard.processCreditCard(
                            "415",#              Vendor 
                            trProcessCreditCardResponse.tokenNumber,#              CcInfoKey             
                            "2.00",#            Amount          
                            "",#                 InvNum         
                            "",#                 ExtData  
                            "UAT" #ServerMode
                    )
        
                    if merchantServiceResponse is not None and (merchantServiceResponse.error is None or merchantServiceResponse.error == ""):
                        print "Message: ", merchantServiceResponse.message + ", AuthCode: " + merchantServiceResponse.authCode + ", PNRef: " + merchantServiceResponse.pnref
                    else:
                        print "Request Failed: " + merchantServiceResponse.error
        else:
            print "Error: Blank response found"