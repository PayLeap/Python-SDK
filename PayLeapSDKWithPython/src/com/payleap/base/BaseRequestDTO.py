'''
Created on Oct 23, 2012

'''

class BaseRequestDTO(object):
    
    def __init__(self, serverMode, userName, password):
        super(BaseRequestDTO, self).__init__()
        #===========================================================================
        # Stores user selected server mode i.e. either UAT or PRODUCTION
        #===========================================================================
        self.serverMode = serverMode  
        #===========================================================================
        # Service user name
        #===========================================================================
        self.userName = userName
        #===========================================================================
        # Service password
        #===========================================================================
        self.password = password 
   
    
    
