class CellRepository(object):
    """A repository of cells.

    Attributes:
        mCells: An internal storage.

    """

    def __init__(self):
        self.mCells = {}

    def addCell(self, aCell):
        self.mCells[aCell.mName] = aCell

    def getCell(self):
        for item in self.mCells.items():
            _, value = item
            if value.mUnderProcess == False:
                if value.mTicksLeft > 0:
                    value.putIntoTheProcessor()
                    return value
        return None
