'''
Created on Oct 23, 2012

'''
from com.payleap.base import BaseRequestDTO

#===============================================================================
# This class will hold the Transaction process credit card request data
#===============================================================================
class ProcessCreditCardDTO(BaseRequestDTO.BaseRequestDTO):   
    
    def __init__(self, transType, cardNum, expDate, nameOnCard, magData, amount, invNum, pnref, 
                 zipCode, street,  state, cvNumber, extData, serverMode, userName, password):
        
        super(BaseRequestDTO, self, serverMode, userName, password).__init__()
        
        #===========================================================================
        # The transaction type being performed.
        #===========================================================================
        self.transType = transType
    
        #===========================================================================
        # Customers card number
        #===========================================================================
        self.cardNum = cardNum
    
        #===========================================================================
        # The expiration date of the credit card used for the transaction in MMYY format.
        #===========================================================================
        self.expDate = expDate
        
        
        #===========================================================================
        # Not used for sale transactions.
        #===========================================================================
        self.invNum = invNum
        
        #===========================================================================
        # The PNRef number of the original Sale transaction.
        #===========================================================================
        self.pnref = pnref
        
        #===========================================================================
        # The cardholder\'s name as printed on the card. 
        #===========================================================================
        self.nameOnCard = nameOnCard
        
        #===========================================================================
        # The cardholder\'s street address. Used for AVS.
        #===========================================================================
        self.street = street
        
        #===========================================================================
        # The cardholder\'s billing ZIP code. Used for AVS.
        #===========================================================================
        self.zipCode = zipCode
        
        #===========================================================================
        # State code of customer
        #===========================================================================
        self.state = state
        
        #===========================================================================
        # The 3-4 digit card verification number. For American Express, four digits displayed on the front of the card; for other card types, usually three digits displayed on the back of the card.
        #===========================================================================
        self.cvNumber = cvNumber  
       
        #===========================================================================
        # The dollar amount of the transaction in DDDDDDDDDD.CC format. This amount includes any tax or tip amounts specified in ExtData.
        #===========================================================================
        self.amount = amount
        
        #===========================================================================
        # For swiped transactions, the complete raw magnetic stripe data from the card wrapped in single quotes.<br/>
        # For example:MagData='%B4111111111111111^BO/JAMES B^14041010000000593000000?; 4111111111111111=14041010000059300000?'
        #===========================================================================
        self.magData = magData
        
        #===============================================================================
        # An XML string containing additional data for the transaction.
        #===============================================================================
        self.extData = extData
        