import logging
import time
import threading

class Processor(threading.Thread):
    """Processor class.
    
    Attributes:
        mCell:   A processed cell.
        mLogger: A logger.
        mName:   A human readable name.
    
    """
    
    def __init__(self, aName):
        self.mLogger = logging.getLogger("ProcessorLogger")
        self.mLogger.setLevel(logging.DEBUG)

        self.mName = aName
        self.mCell = None
        
        threading.Thread.__init__(self)
    
    def setActiveCell(self, aCell):
        self.mCell = aCell
    
    def run(self):
        while True:
            self.mLogger.debug(self.mName + ": is working.")
            if self.mCell != None:
                self.mLogger.debug(self.mName + ": there is a cell: " + self.mCell.mName + ".")
                if self.mCell.mTicksLeft > 0:
                    self.mLogger.debug(self.mName + ": doing work on cell: " + self.mCell.mName + ".")
                    self.mCell.work()
                else:
                    self.mLogger.debug(self.mName + ": removing cell from the processor: " + self.mCell.mName + ".")
                    self.mCell.removeFromTheProcessor()
                    self.mCell = None

            time.sleep(1)
