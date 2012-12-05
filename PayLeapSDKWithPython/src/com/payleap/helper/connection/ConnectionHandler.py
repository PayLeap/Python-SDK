'''
Created on Oct 23, 2012

'''
import httplib
import urllib
from xml.sax import saxutils


class ConnectionHandler:
    
    #===========================================================================
    # This method will take request parameters, service domain and service url call the service and will return the response
    #===========================================================================
    @staticmethod
    def sendHttpPostRequest(paramStr, domain, url):
        data = '';
        print "URL: https://" + (domain + url) 
        print "Params: ", paramStr
        try:
            headers = {"Content-Type" : "application/x-www-form-urlencoded", "Accept" : "text/plain"}
            params = urllib.urlencode(paramStr) 
            conn = httplib.HTTPSConnection(domain)
            conn.request("POST", url, params, headers)
            conn.set_debuglevel(1)
            response = conn.getresponse()
            print "Response Code: ", response.status, ", Response Message: ", response.reason
            data = response.read()
            data = saxutils.unescape(data, {"&apos;": "'", "&quot;": '"', "&lt;" : "<", "&amp;" : "&", "&gt;" : ">"})
        except Exception, e:
            print e.errno     
            print e
            return e
        
        if conn is not None:
            conn.close()
            
        return data
            
#===============================================================================
# paramStr = {
#        "CardNumber": "4111111111111111", 
#        "ExpDate": "1215"
#       }
# 
# data  = ConnectionHandler.sendHttpPostRequest(paramStr, 'uat.payleap.com', '/transactservices.svc/ValidCard')
# print "Response: ", data
#===============================================================================