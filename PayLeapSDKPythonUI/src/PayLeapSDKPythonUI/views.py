'''
Created on Oct 30, 2012

'''


from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from com.payleap.serviceproviders.transaction.TransactionProcessCreditCard import TransactionProcessCreditCard
from com.payleap.serviceproviders.merchant.MerchantAddRecurringCheck import MerchantAddRecurringCheck
from com.payleap.serviceproviders.merchant.MerchantAddRecurringCreditCard import MerchantAddRecurringCreditCard
from com.payleap.serviceproviders.report.ReportGetCardTrx import ReportGetCardTrx
from com.payleap.serviceproviders.report.ReportGetCardTrxSummary import ReportGetCardTrxSummary
from com.payleap.serviceproviders.report.ReportGetCheckTrx import ReportGetCheckTrx
from com.payleap.serviceproviders.report.ReportGetInfo import ReportGetInfo
from com.payleap.serviceproviders.report.ReportGetOpenBatchSummary import ReportGetOpenBatchSummary
from com.payleap.serviceproviders.merchant.MerchantManageCheckInfo import MerchantManageCheckInfo
from com.payleap.serviceproviders.merchant.MerchantManageContract import MerchantManageContract
from com.payleap.serviceproviders.merchant.MerchantManageCreditCardInfo import MerchantManageCreditCardInfo
from com.payleap.serviceproviders.merchant.MerchantManageCustomer import MerchantManageCustomer
from com.payleap.serviceproviders.merchant.MerchantProcessCheck import MerchantProcessCheck
from com.payleap.serviceproviders.transaction.TransactionProcessCheck import TransactionProcessCheck
from com.payleap.serviceproviders.merchant.MerchantProcessCreditCard import MerchantProcessCreditCard
from com.payleap.serviceproviders.transaction.TransactionProcessDebitCard import TransactionProcessDebitCard
from com.payleap.serviceproviders.transaction.TransactionProcessEBTCard import TransactionProcessEBTCard
from com.payleap.serviceproviders.transaction.TransactionProcessGiftCard import TransactionProcessGiftCard
from com.payleap.serviceproviders.transaction.TransactionCardValidation import TransactionCardValidation



#===============================================================================
# Will home page as ProcessCreditCard input form from transaction service
#===============================================================================
def main_page(request):
    template = get_template('transactionProcessCreditCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionCard',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ProcessCreditCard request from Transaction service 
#===============================================================================
def tr_process_credit_card_request(request):   
    
    if request.method == 'POST':
        trProcessCreditCardResponse = TransactionProcessCreditCard.processCreditCard(
                                request.POST['transType'],
                                request.POST['cardNum'],
                                request.POST['expDate'],
                                request.POST['nameOnCard'], 
                                request.POST['magData'], 
                                request.POST['amount'], 
                                request.POST['invNum'], 
                                request.POST['pnref'], 
                                request.POST['zip'], 
                                request.POST['street'], 
                                request.POST['cvNumber'], 
                                request.POST['extData'], 
                                request.POST['serverMode']                                   
        )
          
        if(trProcessCreditCardResponse is not None):
            if isinstance(trProcessCreditCardResponse, Exception):
                resMsg = "Error: " , trProcessCreditCardResponse
            else:
                resMsg = 'Result Code: ' + str(trProcessCreditCardResponse.result) + ', Response: ' + trProcessCreditCardResponse.respMSG + ", Additional Message: " + trProcessCreditCardResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessCreditCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionCard',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ProcessCheck input form from transaction service
#===============================================================================
def tr_process_check_page(request):
    template = get_template('transactionProcessCheck.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionCheck',
    })
    output = template.render(variables)
    return HttpResponse(output)


#===============================================================================
# This method will process the ProcessCheck request from Transaction service 
#===============================================================================
def tr_process_check_request(request):   
    
    if request.method == 'POST':
        trProcessCheckResponse = TransactionProcessCheck.processCheck(
                                request.POST['transType'],
                                request.POST['checkNum'],
                                request.POST['transitNum'],
                                request.POST['accountNum'],
                                request.POST['invNum'],
                                request.POST['amount'],
                                request.POST['micr'],
                                request.POST['nameOnCheck'],
                                request.POST['dl'],
                                request.POST['ss'],
                                request.POST['dob'],
                                request.POST['stateCode'],
                                request.POST['checkType'],
                                request.POST['pnref'],
                                request.POST['magData'],
                                request.POST['extData'],
                                request.POST['serverMode']
        )
          
        if(trProcessCheckResponse is not None):
            if isinstance(trProcessCheckResponse, Exception):
                resMsg = "Error: " , trProcessCheckResponse
            else:
                resMsg = 'Result Code: ' + str(trProcessCheckResponse.result) + ', Response: ' + trProcessCheckResponse.respMSG + ", Additional Message: " + trProcessCheckResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessCheck.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionCheck',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ProcessDebitCard input form from transaction service
#===============================================================================
def tr_process_debit_card_page(request):
    template = get_template('transactionProcessDebitCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionDebit',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ProcessDebitCard request from Transaction service 
#===============================================================================
def tr_process_debit_card_request(request):   
    
    if request.method == 'POST':
        transactionProcessDebitResponse = TransactionProcessDebitCard.processDebitCard(
                                        request.POST['transType'],
                                        request.POST['cardNum'],
                                        request.POST['expDate'],
                                        request.POST['magData'],
                                        request.POST['nameOnCard'],
                                        request.POST['amount'],
                                        request.POST['invNum'],
                                        request.POST['pnref'],
                                        request.POST['pin'],
                                        request.POST['sureChargeAmt'],
                                        request.POST['cashBackAmt'],
                                        request.POST['registerNum'],
                                        request.POST['extData'],
                                        request.POST['serverMode']
        )
          
        if(transactionProcessDebitResponse is not None):
            if isinstance(transactionProcessDebitResponse, Exception):
                resMsg = "Error: " , transactionProcessDebitResponse
            else:
                resMsg = 'Result Code: ' + str(transactionProcessDebitResponse.result) + ', Response: ' + transactionProcessDebitResponse.respMSG + ", Additional Message: " + transactionProcessDebitResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessDebitCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionDebit',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ProcessEBTCard input form from transaction service
#===============================================================================
def tr_process_EBT_card_page(request):
    template = get_template('transactionProcessEBTCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionEBT',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ProcessEBTCard request from Transaction service 
#===============================================================================
def tr_process_EBT_card_request(request):   
    
    if request.method == 'POST':
        transactionProcessEBTResponse = TransactionProcessEBTCard.processEBTCard(
                                        request.POST['transType'],
                                        request.POST['cardNum'],
                                        request.POST['expDate'],
                                        request.POST['magData'],
                                        request.POST['nameOnCard'],
                                        request.POST['amount'],
                                        request.POST['invNum'],
                                        request.POST['pnref'],
                                        request.POST['pin'],
                                        request.POST['sureChargeAmt'],
                                        request.POST['cashBackAmt'],
                                        request.POST['registerNum'],
                                        request.POST['extData'],
                                        request.POST['serverMode']
        )
          
        if(transactionProcessEBTResponse is not None):
            if isinstance(transactionProcessEBTResponse, Exception):
                resMsg = "Error: " , transactionProcessEBTResponse
            else:
                resMsg = 'Result Code: ' + str(transactionProcessEBTResponse.result) + ', Response: ' + transactionProcessEBTResponse.respMSG + ", Additional Message: " + transactionProcessEBTResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessEBTCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionEBT',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)
    
#===============================================================================
# Will home page as ProcessGIFTCard input form from transaction service
#===============================================================================
def tr_process_GIFT_card_page(request):
    template = get_template('transactionProcessGIFTCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionGiftCard',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ProcessGIFTCard request from Transaction service 
#===============================================================================
def tr_process_GIFT_card_request(request):   
    
    if request.method == 'POST':
        transactionProcessGIFTResponse = TransactionProcessGiftCard.processGiftCard(
                                        request.POST['transType'],
                                        request.POST['cardNum'],
                                        request.POST['expDate'],
                                        request.POST['magData'],
                                        request.POST['amount'],
                                        request.POST['invNum'],
                                        request.POST['pnref'],
                                        request.POST['extData'],
                                        request.POST['serverMode']
        )
          
        if(transactionProcessGIFTResponse is not None):
            if isinstance(transactionProcessGIFTResponse, Exception):
                resMsg = "Error: " , transactionProcessGIFTResponse
            else:
                resMsg = 'Result Code: ' + str(transactionProcessGIFTResponse.result) + ', Response: ' + transactionProcessGIFTResponse.respMSG + ", Additional Message: " + transactionProcessGIFTResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessGIFTCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionGiftCard',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ValidCard input form from transaction service
#===============================================================================
def tr_process_Validate_card_page(request):
    template = get_template('transactionProcessValidateCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidCard',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ValidCard request from Transaction service 
#===============================================================================
def tr_process_Validate_card_request(request):   
    
    if request.method == 'POST':
        validationResponse = TransactionCardValidation.processValidCard(
                                        request.POST['cardNum'],
                                        request.POST['expDate'],
                                        request.POST['serverMode']
        )
          
        if(validationResponse is not None):
            if isinstance(validationResponse, Exception):
                resMsg = "Error: " , validationResponse
            else:
                resMsg = 'Response: ' + validationResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessValidateCard.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidCard',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)


#===============================================================================
# Will home page as ValidCardLength input form from transaction service
#===============================================================================
def tr_process_Validate_card_length_page(request):
    template = get_template('transactionProcessValidateCardLength.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidCardLength',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ValidCardLength request from Transaction service 
#===============================================================================
def tr_process_Validate_card_length_request(request):   
    
    if request.method == 'POST':
        validationResponse = TransactionCardValidation.processValidCardLength(
                                        request.POST['cardNum'],
                                        request.POST['serverMode']
        )
          
        if(validationResponse is not None):
            if isinstance(validationResponse, Exception):
                resMsg = "Error: " , validationResponse
            else:
                resMsg = 'Response: ' + validationResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessValidateCardLength.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidCardLength',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ValidExpDate input form from transaction service
#===============================================================================
def tr_process_Validate_Exp_Date_page(request):
    template = get_template('transactionProcessValidateExpDate.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidExpDate',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ValidExpDate request from Transaction service 
#===============================================================================
def tr_process_Validate_Exp_Date_request(request):   
    
    if request.method == 'POST':
        validationResponse = TransactionCardValidation.processValidExpDate(
                                        request.POST['expDate'],
                                        request.POST['serverMode']
        )
          
        if(validationResponse is not None):
            if isinstance(validationResponse, Exception):
                resMsg = "Error: " , validationResponse
            else:
                resMsg = 'Response: ' + validationResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessValidateExpDate.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidExpDate',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ValidMod10 input form from transaction service
#===============================================================================
def tr_process_Validate_Mod10_page(request):
    template = get_template('transactionProcessValidateMod10.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidMod10',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ValidMod10 request from Transaction service 
#===============================================================================
def tr_process_Validate_Mod10_request(request):   
    
    if request.method == 'POST':
        validationResponse = TransactionCardValidation.processValidMod10(
                                        request.POST['cardNum'],
                                        request.POST['serverMode']
        )
          
        if(validationResponse is not None):
            if isinstance(validationResponse, Exception):
                resMsg = "Error: " , validationResponse
            else:
                resMsg = 'Response: ' + validationResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('transactionProcessValidateMod10.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'transactionValidMod10',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)


#===============================================================================
# Will home page as CustomToken Sample input form from transaction service
#===============================================================================
def custom_token_sample_page(request):
    template = get_template('customTokenSample.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'customTokenSample',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the CustomToken Sample request from Transaction service 
#===============================================================================
def custom_token_sample_request(request):   
    
    if request.method == 'POST':
        trProcessCreditCardResponse = TransactionProcessCreditCard.processCreditCard(
                                request.POST['transType'],
                                request.POST['cardNum'],
                                request.POST['expDate'],
                                request.POST['nameOnCard'], 
                                request.POST['magData'], 
                                request.POST['amount'], 
                                request.POST['invNum'], 
                                request.POST['pnref'], 
                                request.POST['zip'], 
                                request.POST['street'], 
                                request.POST['cvNumber'], 
                                request.POST['extData'], 
                                request.POST['serverMode']                                   
        )
          
        if(trProcessCreditCardResponse is not None):
            if isinstance(trProcessCreditCardResponse, Exception):
                resMsg =  "Error: " , trProcessCreditCardResponse
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
                            request.POST['vendor'], 
                            trProcessCreditCardResponse.tokenNumber,#              CcInfoKey             
                            request.POST['amount'],          
                            request.POST['invNum'],         
                            "",  
                            request.POST['serverMode']
                    )
        
                    if merchantServiceResponse is not None and (merchantServiceResponse.error is None or merchantServiceResponse.error == ""):
                        resMsg = "Message: " + merchantServiceResponse.message + ", AuthCode: " + str(merchantServiceResponse.authCode) + ", PNRef: " + str(merchantServiceResponse.pnref)
                    else:
                        resMsg = "Request Failed: " + merchantServiceResponse.error
                else:
                    resMsg = "Error : Result: " + str(trProcessCreditCardResponse.result) + ", RespMSG: " + trProcessCreditCardResponse.respMSG + ", Additional Message: " + trProcessCreditCardResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('customTokenSample.html')
    variables = Context({
        'selectedHeader': 'transaction',
        'selectedSubMenu' : 'customTokenSample',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Merchant Services Started
#===============================================================================

#===============================================================================
# Will home page as AddRecurringCreditCard input form from Merchant service
#===============================================================================
def scm_add_recurring_CC_page(request):
    template = get_template('scmAddRecurringCreditCard.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'addrecurringCreditCard',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the AddRecurringCreditCard request from Merchant service 
#===============================================================================
def scm_add_recurring_CC_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantAddRecurringCreditCard.addRecurringCreditCard(
                                        request.POST['vendor'],
                                        request.POST['customerID'],
                                        request.POST['customerName'],
                                        request.POST['firstName'],
                                        request.POST['lastName'],
                                        request.POST['title'],
                                        request.POST['department'],
                                        request.POST['street1'],
                                        request.POST['street2'],
                                        request.POST['street3'],
                                        request.POST['city'],
                                        request.POST['stateID'],
                                        request.POST['province'],
                                        request.POST['zip'],
                                        request.POST['countryID'],
                                        request.POST['email'],
                                        request.POST['mobile'],
                                        request.POST['contractID'],
                                        request.POST['contractName'],
                                        request.POST['billAmt'],
                                        request.POST['taxAmt'],
                                        request.POST['totalAmt'],
                                        request.POST['startDate'],
                                        request.POST['endDate'],
                                        request.POST['billingPeriod'],
                                        request.POST['billingInterval'],
                                        request.POST['maxFailures'],
                                        request.POST['failureInterval'],
                                        request.POST['emailCustomer'],
                                        request.POST['emailMerchant'],
                                        request.POST['emailCustomerFailure'],
                                        request.POST['emailMerchantFailure'],
                                        request.POST['ccAccountNum'],
                                        request.POST['ccExpdate'],
                                        request.POST['ccNameOnCard'],
                                        request.POST['ccStreet'],
                                        request.POST['ccZip'],
                                        request.POST['extData'],
                                        request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmAddRecurringCreditCard.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'addrecurringCreditCard',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as AddRecurringCheck input form from Merchant service
#===============================================================================
def scm_add_recurring_Check_page(request):
    template = get_template('scmAddRecurringCheck.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'addRecurringCheck',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the AddRecurringCheck request from Merchant service 
#===============================================================================
def scm_add_recurring_Check_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantAddRecurringCheck.addRecurringCheck(
                                        request.POST['vendor'],
                                        request.POST['customerID'],
                                        request.POST['customerName'],
                                        request.POST['firstName'],
                                        request.POST['lastName'],
                                        request.POST['title'],
                                        request.POST['department'],
                                        request.POST['street1'],
                                        request.POST['street2'],
                                        request.POST['street3'],
                                        request.POST['city'],
                                        request.POST['stateID'],
                                        request.POST['province'],
                                        request.POST['zip'],
                                        request.POST['countryID'],
                                        request.POST['email'],
                                        request.POST['mobile'],
                                        request.POST['contractID'],
                                        request.POST['contractName'],
                                        request.POST['billAmt'],
                                        request.POST['taxAmt'],
                                        request.POST['totalAmt'],
                                        request.POST['startDate'],
                                        request.POST['endDate'],
                                        request.POST['billingPeriod'],
                                        request.POST['billingInterval'],
                                        request.POST['maxFailures'],
                                        request.POST['failureInterval'],
                                        request.POST['emailCustomer'],
                                        request.POST['emailMerchant'],
                                        request.POST['emailCustomerFailure'],
                                        request.POST['emailMerchantFailure'],
                                        request.POST['checkType'],
                                        request.POST['accountType'],
                                        request.POST['checkNum'],
                                        request.POST['micr'],
                                        request.POST['accountNum'],
                                        request.POST['transitNum'],
                                        request.POST['ss'],
                                        request.POST['dob'],
                                        request.POST['branchCity'],
                                        request.POST['dl'],
                                        request.POST['stateCode'],
                                        request.POST['nameOnCheck'],
                                        request.POST['extData'],
                                        request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmAddRecurringCheck.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'addRecurringCheck',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ProcessCreditCard input form from Merchant service
#===============================================================================
def scm_process_credit_card_page(request):
    template = get_template('scmProcessCreditCard.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'creditCardRecurringBilling',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ProcessCreditCard request from Merchant service 
#===============================================================================
def scm_process_credit_card_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantProcessCreditCard.processCreditCard(
                                        request.POST['vendor'],
                                        request.POST['ccInfoKey'],
                                        request.POST['amount'],
                                        request.POST['invNum'],
                                        request.POST['extData'],
                                        request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmProcessCreditCard.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'creditCardRecurringBilling',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ProcessCheck input form from Merchant service
#===============================================================================
def scm_process_check_page(request):
    template = get_template('scmProcessCheck.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'checkRecurringBilling',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ProcessCheck request from Merchant service 
#===============================================================================
def scm_process_check_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantProcessCheck.processCheck(
                                        request.POST['vendor'],
                                        request.POST['checkInfoKey'],
                                        request.POST['amount'],
                                        request.POST['invNum'],
                                        request.POST['extData'],
                                        request.POST['serverMode']

        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmProcessCheck.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'checkRecurringBilling',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ManageCheckInfo input form from Merchant service
#===============================================================================
def scm_manage_check_info_page(request):
    template = get_template('scmManageCheckInfo.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageCheckInfo',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ManageCheckInfo request from Merchant service 
#===============================================================================
def scm_manage_check_info_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantManageCheckInfo.manageCheckInfo(
                                    request.POST['transType'],
                                    request.POST['vendor'],
                                    request.POST['customerKey'],
                                    request.POST['checkInfoKey'],
                                    request.POST['checkType'],
                                    request.POST['accountType'],
                                    request.POST['checkNum'],
                                    request.POST['micr'],
                                    request.POST['accountNum'],
                                    request.POST['transitNum'],
                                    request.POST['ss'],
                                    request.POST['dob'],
                                    request.POST['branchCity'],
                                    request.POST['dl'],
                                    request.POST['stateCode'],
                                    request.POST['nameOnCheck'],
                                    request.POST['email'],
                                    request.POST['dayPhone'],
                                    request.POST['street1'],
                                    request.POST['street2'],
                                    request.POST['street3'],
                                    request.POST['city'],
                                    request.POST['stateID'],
                                    request.POST['province'],
                                    request.POST['postalCode'],
                                    request.POST['countryID'],
                                    request.POST['extData'],
                                    request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmManageCheckInfo.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageCheckInfo',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ManageCreditCardInfo input form from Merchant service
#===============================================================================
def scm_manage_credit_card_info_page(request):
    template = get_template('scmManageCreditCardInfo.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageCreditInfo',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ManageCreditCardInfo request from Merchant service 
#===============================================================================
def scm_manage_credit_card_info_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantManageCreditCardInfo.manageCreditCardInfo(
                                    request.POST['transType'],
                                    request.POST['vendor'],
                                    request.POST['customerKey'],
                                    request.POST['cardInfoKey'],
                                    request.POST['ccAccountNum'],
                                    request.POST['ccExpDate'],
                                    request.POST['ccNameonCard'],
                                    request.POST['ccStreet'],
                                    request.POST['ccZip'],
                                    request.POST['extData'],
                                    request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmManageCreditCardInfo.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageCreditInfo',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ManageContract input form from Merchant service
#===============================================================================
def scm_manage_contract_page(request):
    template = get_template('scmManageContract.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageContract',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ManageContract request from Merchant service 
#===============================================================================
def scm_manage_contract_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantManageContract.manageContract(
                                    request.POST['transType'],
                                    request.POST['vendor'],
                                    request.POST['customerKey'],
                                    request.POST['contractKey'],
                                    request.POST['paymentInfoKey'],
                                    request.POST['paymentType'],
                                    request.POST['customerID'],
                                    request.POST['customerName'],
                                    request.POST['firstName'],
                                    request.POST['lastName'],
                                    request.POST['title'],
                                    request.POST['department'],
                                    request.POST['street1'],
                                    request.POST['street2'],
                                    request.POST['street3'],
                                    request.POST['city'],
                                    request.POST['stateID'],
                                    request.POST['province'],
                                    request.POST['zip'],
                                    request.POST['countryID'],
                                    request.POST['email'],
                                    request.POST['dayPhone'],
                                    request.POST['nightPhone'],
                                    request.POST['fax'],
                                    request.POST['mobile'],
                                    request.POST['contractID'],
                                    request.POST['contractName'],
                                    request.POST['billAmt'],
                                    request.POST['taxAmt'],
                                    request.POST['totalAmt'],
                                    request.POST['startDate'],
                                    request.POST['endDate'],
                                    request.POST['nextBillDt'],
                                    request.POST['billingPeriod'],
                                    request.POST['billingInterval'],
                                    request.POST['maxFailures'],
                                    request.POST['failureInterval'],
                                    request.POST['emailCustomer'],
                                    request.POST['emailMerchant'],
                                    request.POST['emailCustomerFailure'],
                                    request.POST['emailMerchantFailure'],
                                    request.POST['status'],
                                    request.POST['extData'],
                                    request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmManageContract.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageContract',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as ManageCustomer input form from Merchant service
#===============================================================================
def scm_manage_customer_page(request):
    template = get_template('scmManageCustomer.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageCustomer',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the ManageCustomer request from Merchant service 
#===============================================================================
def scm_manage_customer_request(request):   
    
    if request.method == 'POST':
        merchantServiceResponse = MerchantManageCustomer.manageCustomer(
                                    request.POST['transType'],
                                    request.POST['vendor'],
                                    request.POST['customerKey'],
                                    request.POST['customerID'],
                                    request.POST['customerName'],
                                    request.POST['firstName'],
                                    request.POST['lastName'],
                                    request.POST['title'],
                                    request.POST['department'],
                                    request.POST['street1'],
                                    request.POST['street2'],
                                    request.POST['street3'],
                                    request.POST['city'],
                                    request.POST['stateID'],
                                    request.POST['province'],
                                    request.POST['zip'],
                                    request.POST['countryID'],
                                    request.POST['dayPhone'],
                                    request.POST['nightPhone'],
                                    request.POST['fax'],
                                    request.POST['email'],
                                    request.POST['mobile'],
                                    "",
                                    request.POST['extData'],
                                    request.POST['serverMode']
        )
          
        if(merchantServiceResponse is not None):
            if isinstance(merchantServiceResponse, Exception):
                resMsg = "Error: " , merchantServiceResponse
            else:
                if merchantServiceResponse.error is not None and merchantServiceResponse.error != '':
                    resMsg = "Error: " + merchantServiceResponse.error
                else:
                    resMsg = 'Response Code: ' + str(merchantServiceResponse.code) + ", Result: " + merchantServiceResponse.result + ", Message: " + merchantServiceResponse.message
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request" 
    
    template = get_template('scmManageCustomer.html')
    variables = Context({
        'selectedHeader': 'merchant',
        'selectedSubMenu' : 'manageCustomer',
        'resMsg' : resMsg
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Report Services started
#===============================================================================

#===============================================================================
# Will home page as GetCardTrx input form from Report service
#===============================================================================
def report_get_card_trx_page(request):
    template = get_template('reportGetCardTrx.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getCardTrx',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the GetCardTrx request from Report service 
#===============================================================================
def report_get_card_trx_request(request):   
    listFlag = 0
    if request.method == 'POST':
        cardTrxResponse = ReportGetCardTrx.getCardTrx(
                                    request.POST['rpnum'],
                                    request.POST['pnref'],
                                    request.POST['beginDt'],
                                    request.POST['endDt'],
                                    request.POST['paymentType'],
                                    request.POST['excludePaymentType'],
                                    request.POST['transType'],
                                    "", #request.POST['excludeTransType'],
                                    request.POST['approvalCode'],
                                    request.POST['result'],
                                    request.POST['excludeResult'],
                                    request.POST['nameOnCard'],
                                    request.POST['cardNum'],
                                    request.POST['cardType'],
                                    request.POST['excludeCardType'],
                                    request.POST['excludeVoid'],
                                    request.POST['user'],
                                    request.POST['invoiceId'],
                                    request.POST['settleFlag'],
                                    request.POST['settleMsg'],
                                    request.POST['settleDt'],
                                    "", #request.POST['transformType'],
                                    "", #request.POST['xsl'],
                                    "", #request.POST['colDelim'],
                                    "", #request.POST['rowDelim'],
                                    "", #request.POST['includeHeader'],
                                    request.POST['extData'],
                                    request.POST['serverMode']
        )
        
        if(cardTrxResponse is not None):
            if isinstance(cardTrxResponse, Exception):
                resMsg =  "Error: " , cardTrxResponse
            else:
                if isinstance(cardTrxResponse, list):
                    resMsg = cardTrxResponse
                    listFlag = 1
                else:
                    resMsg = "Error Msg: ",cardTrxResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request"   
        
    template = get_template('reportGetCardTrx.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getCardTrx',
        'resMsg' : resMsg,
        'listFlag' : listFlag
    })
    output = template.render(variables)
    return HttpResponse(output)


#===============================================================================
# Will home page as GetCardTrxSummary input form from Report service
#===============================================================================
def report_get_card_trx_summary_page(request):
    template = get_template('reportGetCardTrxSummary.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getCardTrxSummery',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the GetCardTrxSummary request from Report service 
#===============================================================================
def report_get_card_trx_summary_request(request):   
    listFlag = 0
    if request.method == 'POST':
        cardTrxSummeryResp = ReportGetCardTrxSummary.getCardTrxSummary(
                                request.POST['rpnum'],
                                request.POST['beginDt'],
                                request.POST['endDt'],
                                request.POST['approvalCode'],
                                request.POST['register'],
                                request.POST['nameOnCard'],
                                request.POST['cardNum'],
                                request.POST['cardType'],
                                request.POST['excludeVoid'],
                                request.POST['user'],
                                request.POST['settleFlag'],
                                request.POST['settleMsg'],
                                request.POST['settleDt'],
                                "", #request.POST['transformType'],
                                "", #request.POST['xsl'],
                                "", #request.POST['colDelim'],
                                "", #request.POST['rowDelim'],
                                "", #request.POST['includeHeader'],
                                request.POST['extData'],
                                request.POST['serverMode']

        )
        
        if(cardTrxSummeryResp is not None):
            if isinstance(cardTrxSummeryResp, Exception):
                resMsg =  "Error: " , cardTrxSummeryResp
            else:
                if isinstance(cardTrxSummeryResp, list):
                    resMsg = cardTrxSummeryResp
                    listFlag = 1
                else:
                    resMsg = "Error Msg: ",cardTrxSummeryResp
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request"   
        
    template = get_template('reportGetCardTrxSummary.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getCardTrxSummery',
        'resMsg' : resMsg,
        'listFlag' : listFlag
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as GetCheckTrx input form from Report service
#===============================================================================
def report_get_check_trx_page(request):
    template = get_template('reportGetCheckTrx.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getCheckTrx',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the GetCheckTrx request from Report service 
#===============================================================================
def report_get_check_trx_request(request):   
    listFlag = 0
    if request.method == 'POST':
        checkTrxResponse = ReportGetCheckTrx.getCheckTrx(
                            request.POST['rpnum'],
                            request.POST['pnref'],
                            request.POST['beginDt'],
                            request.POST['endDt'],
                            request.POST['paymentType'],
                            request.POST['excludePaymentType'],
                            request.POST['transType'],
                            request.POST['excludeTransType'],
                            request.POST['approvalCode'],
                            request.POST['result'],
                            request.POST['excludeResult'],
                            request.POST['nameOnCheck'],
                            request.POST['checkNum'],
                            request.POST['acctNum'],
                            request.POST['routeNum'],
                            request.POST['excludeVoid'],
                            request.POST['user'],
                            request.POST['invoiceId'],
                            request.POST['settleFlag'],
                            request.POST['settleMsg'],
                            request.POST['settleDt'],
                            "", #request.POST['transformType'],
                            "", #request.POST['xsl'],
                            "", #request.POST['colDelim'],
                            "", #request.POST['rowDelim'],
                            "", #request.POST['includeHeader'],
                            request.POST['extData'],
                            request.POST['serverMode']
        )
        
        if(checkTrxResponse is not None):
            if isinstance(checkTrxResponse, Exception):
                resMsg =  "Error: " , checkTrxResponse
            else:
                if isinstance(checkTrxResponse, list):
                    resMsg = checkTrxResponse
                    listFlag = 1
                else:
                    resMsg = "Error Msg: ",checkTrxResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request"   
        
    template = get_template('reportGetCheckTrx.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getCheckTrx',
        'resMsg' : resMsg,
        'listFlag' : listFlag
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as GetInfo input form from Report service
#===============================================================================
def report_get_info_page(request):
    template = get_template('reportGetInfo.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getInfo',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the GetInfo request from Report service 
#===============================================================================
def report_get_info_request(request):   
    listFlag = 0
    if request.method == 'POST':
        infoserviceResponse = ReportGetInfo.getInfo(
                            request.POST['transType'],
                            request.POST['extData'],
                            request.POST['serverMode']
        )
        
        if(infoserviceResponse is not None):
            if isinstance(infoserviceResponse, Exception):
                resMsg =  "Error: " , infoserviceResponse
            else:
                if isinstance(infoserviceResponse, list):
                    resMsg = infoserviceResponse
                    listFlag = 1
                else:
                    resMsg = "Error Msg: ",infoserviceResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request"   
        
    template = get_template('reportGetInfo.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getInfo',
        'resMsg' : resMsg,
        'listFlag' : listFlag
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# Will home page as GetOpenBatchSummary input form from Report service
#===============================================================================
def report_get_open_batch_summary_page(request):
    template = get_template('reportGetOpenBatchSummary.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getOpenBatchSummery',
    })
    output = template.render(variables)
    return HttpResponse(output)

#===============================================================================
# This method will process the GetOpenBatchSummary request from Report service 
#===============================================================================
def report_get_open_batch_summary_request(request):   
    listFlag = 0
    if request.method == 'POST':
        openBatchSummaryResponse = ReportGetOpenBatchSummary.getOpenBatchSummary(
                                    request.POST['rpnum'],
                                    request.POST['beginDt'],
                                    request.POST['endDt'],
                                    "", #request.POST['extData'],
                                    request.POST['serverMode']
        )
        
        if(openBatchSummaryResponse is not None):
            if isinstance(openBatchSummaryResponse, Exception):
                resMsg =  "Error: " , openBatchSummaryResponse
            else:
                if isinstance(openBatchSummaryResponse, list):
                    resMsg = openBatchSummaryResponse
                    listFlag = 1
                else:
                    resMsg = "Error Msg: ",openBatchSummaryResponse
        else:
            resMsg = "Error: Blank response found"
    else:
        resMsg = "Error: Please submit the form using POST request"   
        
    template = get_template('reportGetOpenBatchSummary.html')
    variables = Context({
        'selectedHeader': 'report',
        'selectedSubMenu' : 'getOpenBatchSummery',
        'resMsg' : resMsg,
        'listFlag' : listFlag
    })
    output = template.render(variables)
    return HttpResponse(output)
