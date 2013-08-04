import Cell
import Processor

class VM(object):
    """VM class.
    
    Attributes:
        mCells:      An array of cells.
        mProcessors: An array of processors.
    
    """
    
    def __init__(self):
        self.mCells = []
        for i in range(10):
            self.mCells.append(Cell.Cell("Cell" + str(i)))
        
        self.mProcessors = []
        for i in range(10):
            self.mProcessors.append(Processor.Processor("Processor" + str(i)))
            self.mProcessors[i].setDaemon(True)
            self.mProcessors[i].start()

    def run(self):
        while True:
            for i in range(10):
                self.mProcessors[i].setActiveCell(self.mCells[i])

        for i in range(10):
            self.mProcessors[i].join()

if __name__ == "__main__":
    vm = VM()
    vm.run()
