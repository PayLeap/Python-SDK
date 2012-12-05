import os.path
from django.conf.urls.defaults import *
from PayLeapSDKPythonUI.views import *

#Path to static data files e.g. css, images etc
site_media = os.path.join(
    os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
    
    #Transaction URLS
    (r'^$', main_page),
    (r'^transactionProcessCreditCardPage/$', main_page),    
    (r'^transactionProcessCreditCardRequest/$', tr_process_credit_card_request),
    (r'^transactionProcessCheckPage/$', tr_process_check_page),
    (r'^transactionProcessCheckRequest/$', tr_process_check_request),
    (r'^transactionProcessDebitCardPage/$', tr_process_debit_card_page),
    (r'^transactionProcessDebitCardRequest/$', tr_process_debit_card_request),
    (r'^transactionProcessEBTCardPage/$', tr_process_EBT_card_page),
    (r'^transactionProcessEBTCardRequest/$', tr_process_EBT_card_request),
    (r'^transactionProcessGiftCardPage/$', tr_process_GIFT_card_page),
    (r'^transactionProcessGiftCardRequest/$', tr_process_GIFT_card_request),
    (r'^transactionProcessValidateCardPage/$', tr_process_Validate_card_page),
    (r'^transactionProcessValidateCardRequest/$', tr_process_Validate_card_request),
    (r'^transactionProcessValidCardLengthPage/$', tr_process_Validate_card_length_page),
    (r'^transactionProcessValidCardLengthRequest/$', tr_process_Validate_card_length_request),
    (r'^transactionProcessValidExpDatePage/$', tr_process_Validate_Exp_Date_page),
    (r'^transactionProcessValidExpDateRequest/$', tr_process_Validate_Exp_Date_request),
    (r'^transactionProcessValidMod10Page/$', tr_process_Validate_Mod10_page),
    (r'^transactionProcessValidMod10Request/$', tr_process_Validate_Mod10_request),
    (r'^customTokenSamplePage/$', custom_token_sample_page),
    (r'^customTokenSampleRequest/$', custom_token_sample_request),
    
    #Merchant services
    (r'^scmAddRecurringCreditCardPage/$', scm_add_recurring_CC_page),
    (r'^scmAddRecurringCreditCardRequest/$', scm_add_recurring_CC_request),
    (r'^scmAddRecurringCheckPage/$', scm_add_recurring_Check_page),
    (r'^scmAddRecurringCheckRequest/$', scm_add_recurring_Check_request),
    (r'^scmProcessCreditCardPage/$', scm_process_credit_card_page),
    (r'^scmProcessCreditCardRequest/$', scm_process_credit_card_request),
    (r'^scmProcessCheckPage/$', scm_process_check_page),
    (r'^scmProcessCheckRequest/$', scm_process_check_request),
    (r'^scmManageCheckInfoPage/$', scm_manage_check_info_page),
    (r'^scmManageCheckInfoRequest/$', scm_manage_check_info_request),
    (r'^scmManageCreditCardInfoPage/$', scm_manage_credit_card_info_page),
    (r'^scmManageCreditCardInfoRequest/$', scm_manage_credit_card_info_request),
    (r'^scmManageContractPage/$', scm_manage_contract_page),
    (r'^scmManageContractRequest/$', scm_manage_contract_request),
    (r'^scmManageCustomerPage/$', scm_manage_customer_page),
    (r'^scmManageCustomerRequest/$', scm_manage_customer_request),
    
    #Report Services
    (r'^reportGetCardTrxPage/$', report_get_card_trx_page),
    (r'^reportGetCardTrxRequest/$', report_get_card_trx_request),
    (r'^reportGetCardTrxSummaryPage/$', report_get_card_trx_summary_page),
    (r'^reportGetCardTrxSummaryRequest/$', report_get_card_trx_summary_request),
    (r'^reportGetCheckTrxPage/$', report_get_check_trx_page),
    (r'^reportGetCheckTrxRequest/$', report_get_check_trx_request),
    (r'^reportGetInfoPage/$', report_get_info_page),
    (r'^reportGetInfoRequest/$', report_get_info_request),
    (r'^reportGetOpenBatchSummaryPage/$', report_get_open_batch_summary_page),
    (r'^reportGetOpenBatchSummaryRequest/$', report_get_open_batch_summary_request),
    #Static resource mapping changes
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
)