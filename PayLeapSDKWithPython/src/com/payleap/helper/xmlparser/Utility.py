'''
Created on Oct 25, 2012

'''
import string

class Utility:
    
    @staticmethod
    def retriveFromXMLTag(xmlStr, tagName):
        startTag = "<" + tagName + ">"
        endTag = "</" + tagName + ">"
        
        startIndex = string.find(xmlStr, startTag)
        endIndex = string.find(xmlStr, endTag)
        
        if startIndex == -1 or endIndex == -1:
            return "";
        
        subStrBeginIndx = startIndex + len(startTag)
        subStrEndIndx = subStrBeginIndx + (endIndex - startIndex - len(startTag))
        return xmlStr[subStrBeginIndx:subStrEndIndx]