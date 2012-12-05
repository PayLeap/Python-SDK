'''
Created on Oct 29, 2012

'''

from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.report.GetOpenBatchSummaryRespParser import GetOpenBatchSummaryRespParser

class ReportGetOpenBatchSummary:
    """This class will processes GetOpenBatchSummary service to retrieve the payment type transaction summary of the current open batch for a merchant"""
    
    @staticmethod
    def getOpenBatchSummary(rPNum, beginDt, endDt, extData, serverMode):
        r"""This method will help build to the GetOpenBatchSummary request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            rPNum (str): Your PayLeap Vendor number that uniquely identifies your merchant account. |br|
            beginDt (str): The begin date of the date range in MM/DD/YYYY format. This date will be converted to: MM/DD/YYYYT00:00:00:0000AM |br|
            endDt (str): The end date of the date range in MM/DD/YYYY format. This date will be converted to: MM/DD/YYYYT12:59:59:9999PM |br|
            extData (str): Not used for this operation. |br|
            serverMode (str): Valid values are: PRODUCTION, UAT. |br|
        Returns:
           GetOpenBatchSummaryRespParser. Will populated using XML response.   
    
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
                    "BeginDt" : beginDt,
                    "EndDt" : endDt,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/reportingservices.svc/GetOpenBatchSummary')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            openBatchSummaryResponse = GetOpenBatchSummaryRespParser.parser(response);
            return openBatchSummaryResponse;
        else:
            return None