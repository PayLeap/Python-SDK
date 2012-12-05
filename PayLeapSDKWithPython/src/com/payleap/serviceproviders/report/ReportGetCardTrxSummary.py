'''
Created on Oct 29, 2012

'''

from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.report.GetCardTrxSummaryRespParser import GetCardTrxSummaryRespParser

class ReportGetCardTrxSummary:
    """This class will processes GetCardTrxSummary service to retrieve a summary of card payments for a merchant"""
    
    @staticmethod
    def getCardTrxSummary(rPNum, beginDt, endDt, approvalCode, register, nameOnCard, cardNum, cardType, excludeVoid, 
                user, settleFlag, settleMsg, settleDt, transformType, xsl, colDelim, rowDelim, 
                includeHeader, extData, serverMode):
        r"""This method will help to build the GetCardTrxSummary request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:  
            rPNum (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br| 
            beginDt (str): The begin date of the date range in MM/DD/YYYY format. |br| 
            endDt (str): The inclusive end date of the date range in MM/DD/YYYY format. |br| 
            approvalCode (str): The code returned by PayLeap for approved transactions. If provided, only those transactions matching the ApprovalCode parameter will be included. |br| 
            register (str): The register that originated the transaction. If provided, only those transactions with the matching register will be included. |br| 
            nameOnCard (str): Cardholder's name as it is appears on the card. If provided, only those transactions with cardholder's name matching NameOnCard will be included. This parameter uses partial matching. For example: "test" matches "test","1test" and "1test234". |br| 
            cardNum (str): A card number. If provided, only those transactions with the cardholder's name matching CardNum will be included. This parameter uses partial matching. |br| 
            cardType (str): A type of credit card. If provided, only those transactions matching the CardType will be included. See Card Type Request Codes on page 35 for valid values. |br| 
            To include multiple payment types, submit each desired type separated by commas. For example, "'VISA,MASTER,DISCOVER" will pull all transactions with either VISA, MASTER and DISCOVER card type. |br| 
            excludeVoid (str): An option to exclude voided transactions. Valid values are: TRUE or FALSE. The default value is TRUE. |br| 
            user (str): The user who originated the transactions. If provided, only those transactions created by the matching User will be included. This parameter uses partial matching. |br| 
            settleFlag (str): An option to retrieve the settled transactions or unsettled transactions. Valid values are: TRUE or FALSE. |br| 
            settleMsg (str): The settlement ID or message returned from the host. |br| 
            settleDt (str): The settlement timestamp in MM/DD/YYYYT00:00:00AM format. |br| 
            transformType (str): The type of format to transform the data into. Currently only supporting XML type |br| 
            xsl (str): Not using for this transformType |br| 
            colDelim (str): Not using for this transformType |br| 
            rowDelim (str): Not using for this transformType |br| 
            includeHeader (str): Not using for this transformType |br| 
            extData (str): Not used for this operation. |br|        
            serverMode (str): Valid values are: PRODUCTION, UAT. |br|
            
        Returns:
           GetCardTrxSummaryRespParser. Will populated using XML response.   
    
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
                    "RPNum"  : rPNum,
                    "BeginDt"  : beginDt,
                    "EndDt"  : endDt,
                    "ApprovalCode"  : approvalCode, 
                    "Register"  : register,
                    "NameOnCard"  : nameOnCard,
                    "CardNum"  : cardNum,
                    "CardType"  : cardType,
                    "ExcludeVoid"  : excludeVoid,
                    "User"  : user,
                    "SettleFlag"  : settleFlag, 
                    "SettleMsg"  : settleMsg,
                    "SettleDt"  : settleDt,
                    "TransformType"  : "",
                    "Xsl"  : "",
                    "ColDelim"  : "", 
                    "RowDelim"  : "",
                    "IncludeHeader"  : "", 
                    "ExtData"  : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/reportingservices.svc/GetCardTrxSummary')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            cardTrxSummaryRespParser = GetCardTrxSummaryRespParser.parser(response);
            return cardTrxSummaryRespParser;
        else:
            return None