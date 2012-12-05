'''
Created on Oct 29, 2012

'''

from com.payleap.constants.Constants import ConstantResources
from com.payleap.helper.connection.ConnectionHandler import ConnectionHandler
from com.payleap.helper.xmlparser.report.GetInfoRespParser import GetInfoRespParser

class ReportGetInfo:
    """This class will processes GetInfo service to retrieve information related to your merchant account"""
    
    @staticmethod
    def getInfo(transType, extData, serverMode):
        r"""This method will help to build the GetInfo request, to send the same request and after getting it's response will extract it's data and will return the response   

        Args:    
            transType (str): The transaction type being performed. |br|
            extData (str): An XML string containing additional data for the transaction. See the following section for more information. |br|
            serverMode (str): Valid values are: PRODUCTION, UAT. |br|
        Returns:
           GetInfoRespParser. Will populated using XML response.   
    
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
                    "TransType" : transType,
                    "ExtData" : extData
        }
        response = ConnectionHandler.sendHttpPostRequest(paramStr, domain, '/reportingservices.svc/GetInfo')
        
        if isinstance(response, Exception):
            return response
        elif response is not None and response != "":
            infoResponse = GetInfoRespParser.parser(response);
            return infoResponse;
        else:
            return None