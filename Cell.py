class Cell(object):
    """Cell class.
    
    The main construction unit.
    
    Attributes:
        mName: A human readable name.
        
    """
    
    def __init__(self, aName):
        self.mName = aName

    def work(self):
        print("My name is " + self.mName + ". I am just doing my work.")
