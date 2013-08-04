import logging 

class Cell(object):
    """Cell class.

    The main construction unit.

    Attributes:
        mName:         A human readable name.
        mUnderProcess: Whether the cell is under process.
        mTicksLeft:    How long the cell will be processed.
        mCellLogger:   

    """

    def __init__(self, aName):
        self.mLogger = logging.getLogger("CellLogger")
        self.mLogger.setLevel(logging.DEBUG)

        self.mName         = aName
        self.mUnderProcess = False
        self.mTicksLeft    = 5

    def putIntoTheProcessor(self):
        self.mUnderProcess = True

    def removeFromTheProcessor(self):
        self.mUnderProcess = False

    def work(self):
        self.mLogger.debug(self.mName + ": just doing my work.")
        self.mTicksLeft = self.mTicksLeft - 1
