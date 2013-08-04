import time
import threading

class Processor(threading.Thread):
    """Processor class.
    
    Attributes:
        mCell: A processed cell.
        mName: A human readable name.
    
    """
    
    def __init__(self, aName):
        self.mName = aName
        self.mCell = None
        
        threading.Thread.__init__(self)
    
    def setActiveCell(self, aCell):
        self.mCell = aCell
    
    def run(self):
        while True:
            time.sleep(1)
            print("Processor: " + self.mName)
            if self.mCell != None:
                self.mCell.work()
