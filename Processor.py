import time
import threading

class Processor(threading.Thread):
    """Processor class.
    
    Attributes:
        mName: Human readable name.
    
    """
    
    def __init__(self, aName):
        self.mName = aName
        
        threading.Thread.__init__(self, self.mName)
    
    def run(self):
        while True:
            time.sleep(1)
            print("Processor: " + self.mName)
