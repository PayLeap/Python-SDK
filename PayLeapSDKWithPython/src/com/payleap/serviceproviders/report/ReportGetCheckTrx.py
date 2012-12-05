'''
Created on Oct 29, 2012

'''

from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.report.GetCheckTrxRespParser import GetCheckTrxRespParser

class ReportGetCheckTrx:
    """This class will processes GetCheckTrx service To retrieve check transaction details for a merchant"""
    
    @staticmethod
    def getCheckTrx(rPNum, pNRef, beginDt, endDt, paymentType, excludePaymentType, transType, excludeTransType, 
                approvalCode, result, excludeResult, nameOnCheck, checkNum, acctNum, routeNum, excludeVoid, 
                user, invoiceId, settleFlag, settleMsg, settleDt, transformType, xsl, colDelim, rowDelim, 
                includeHeader, extData, serverMode):
        r"""This method will help to build the GetCheckTrx request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            rPNum (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            pNRef (str): To search for a single transaction, provide the unique payment reference number assigned to the transaction. If this field is provided, all other query fields are ignored. |br| 
            beginDt (str): The begin date of the date range in MM/DD/YYYY (or YYYY-MM-DD or YYYY-MM-DDThh:mm:ss) format. This date will be converted to YYYY-MM-DDThh:mm:ss (time is in 24-hour format). If the submitted value does not contain time information, BeginDt defaults to midnight on the given date. For example: |br| 
            2005-08-19T12:00:12 is kept as is. |br| 
            2005-08-19 becomes 2005-08-19T00:00:00. |br| 
            2005/08/19 becomes 2005-08-19T00:00:00. |br| 
            08/19/2005 becomes 2005-08-19T00:00:00. |br| 
            The reporting service returns transactions whose date is greater than or equal to the begin date. |br| 
            endDt (str): The end date of the date range in MM/DD/YYYY (or YYYY-MM-DD or YYYY-MM-DDThh:mm:ss) format. This date will be converted to YYYY-MM-DDThh:mm:ss (time is in 24-hour format). If the submitted value does not contain time information, EndDt increments to the next day at midnight, such that no transaction on the desired end date will be excluded based on its time. For example: |br| 
            2005-08-19T12:00:12 is kept as is. |br| 
            2005-08-19 becomes 2005-08-20T00:00:00. |br| 
            08/19/2005 becomes 2005-08-20T00:00:00. |br| 
            The reporting service returns transactions whose date is less than the end date. |br| 
            paymentType (str): The type of card used for payment. If provided, only those transactions matching the PaymentType will be included. |br| 
            To include multiple payment types, submit each desired type separated by commas. For example, "ACH, ECHECK" will pull all transactions with either ACH or ECHECK payment types. |br| 
            excludePaymentType (str): Indicates which PaymentType(s) to exclude from the response. If provided, any transaction matching the ExcludePaymentType will be excluded. |br| 
            transType (str): The transaction type being performed. If provided, only those transactions matching the TransType will be included. |br| 
            To include multiple payment types, submit each desired type separated by commas. For example: "Credit,Sale" will pull all transactions with either Credit or Sale transaction types. |br| 
            excludeTransType (str): Indicates which TransType(s) to exclude from the response. If provided, any transaction matching the ExcludeTransType will be excluded. |br| 
            approvalCode (str): The code returned by PayLeap for approved transactions. If provided, only those transactions matching the ApprovalCode parameter will be included. |br| 
            result (str): The transaction result code from PayLeap. If provided, only those transactions matching the Result will be included. Valid values are: |br| 
            0 (approved) |br| 
            All other values represent a declined transaction. To return all declined transactions, you should leave this field empty and set the ExcludeResult to 0 instead. |br| 
            excludeResult (str): Indicates which Result code(s) to exclude from the response. If provided, any transactions matching the ExcludeResult will be excluded. |br| 
            nameOnCheck (str): The customer's name as it is appears on the check, if provided. Only those transactions with the customer's name matching NameOnCheck will be included. This parameter uses partial matching. For example: "test" matches "test","1test" and "1test234". |br| 
            checkNum (str): A check number. If provided, only those transactions with matching CheckNum will be included. |br| 
            acctNum (str): The customer's checking account number. If provided, only those transactions matching the AcctNum will be included. This parameter uses partial matching. |br| 
            routeNum (str): The routing number printed on the check. Any transactions matching the RouteNum (Transit Number) will be included. This parameter uses partial matching. |br| 
            excludeVoid (str): An option to exclude voided transactions. Valid values are: TRUE or FALSE. The default value is TRUE. |br| 
            user (str): The user who originated the transactions. If provided, only those transactions created by the matching User will be included. This parameter uses partial matching. |br| 
            invoiceId (str): The invoice ID that was included in the original transaction. If provided, only those transactions with matching InvoiceId will be included. This parameter uses partial matching. |br| 
            settleFlag (str): An option to retrieve the settled or unsettled transactions. Valid values are: TRUE or FALSE. |br| 
            settleMsg (str): The settlement ID or message returned from the host. |br| 
            settleDt (str): The settlement timestamp in MM/DD/YYYYT00:00:00AM format. |br| 
            transformType (str): The type of format to transform the data into. Currently only supporting XML type |br|  |br| 
            xsl (str): Not using for this transformType |br| 
            colDelim (str): Not using for this transformType |br| 
            rowDelim (str): Not using for this transformType |br| 
            includeHeader (str): Not using for this transformType |br| 
            extData (str): An XML string containing additional data for the transaction. See the following section for more information. |br|   
            serverMode (str): Valid values are: PRODUCTION, UAT. |br|
        Returns:
           GetCheckTrxRespParser. Will populated using XML response.   
    
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
                    "UserName" : userName,
                    "Password" : password,
                    "RPNum" : rPNum,
                    "PNRef" : pNRef,
                    "BeginDt" : beginDt,
                    "EndDt" : endDt,
                    "PaymentType" : paymentType,
                    "ExcludePaymentType" : excludePaymentType,
                    "TransType" : transformType,
                    "ExcludeTransType" : excludeTransType,
                    "ApprovalCode" : approvalCode,
                    "Result" : result,
                    "ExcludeResult" : excludeResult,
                    "NameOnCheck" : nameOnCheck,
                    "CheckNum" : checkNum,
                    "AcctNum" : acctNum, 
                    "RouteNum" : routeNum,
                    "ExcludeVoid" : excludeVoid,
                    "User" : user,
                    "InvoiceId" : invoiceId,
                    "SettleFlag" : settleFlag,
                    "SettleMsg" : settleMsg,
                    "SettleDt" : settleDt,
                    "TransformType" : "",
                    "Xsl" : "",
                    "ColDelim" : "", 
                    "RowDelim" : "", 
                    "IncludeHeader" : "", 
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/reportingservices.svc/GetCheckTrx')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            checkTrxResponse = GetCheckTrxRespParser.parser(response);
            return checkTrxResponse;
        else:
            return None