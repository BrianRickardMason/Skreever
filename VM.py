import logging
import time

import Cell
import CellRepository
import Processor

logging.basicConfig(format='[%(asctime)s][%(threadName)28s][%(levelname)8s] - %(message)s')

class VM(object):
    """VM class.

    Attributes:
        mCellRepository: A repository of cells.
        mProcessors:     An array of processors.
        mLogger:         A logger.

    """

    def __init__(self):
        self.mLogger = logging.getLogger("VMLogger")
        self.mLogger.setLevel(logging.DEBUG)

        self.mCellRepository = CellRepository.CellRepository()

        self.mLogger.debug("Creating cells.")
        for i in range(50):
            cellName = "Cell" + str(i)
            self.mLogger.debug("Creating a cell: " + cellName + ".")
            self.mCellRepository.addCell(Cell.Cell(cellName))

        self.mLogger.debug("Creating processors.")
        self.mProcessors = []
        for i in range(10):
            processorName = "Processor" + str(i)
            self.mLogger.debug("Creating a processor: " + processorName + ".")
            self.mProcessors.append(Processor.Processor(processorName))
            self.mProcessors[i].setDaemon(True)
            self.mProcessors[i].start()

    def run(self):
        while True:
            for i in range(10):
                if self.mProcessors[i].mCell == None:
                    cell = self.mCellRepository.getCell()
                    if cell != None:
                        self.mProcessors[i].setActiveCell(cell)
            time.sleep(1)

        for i in range(10):
            self.mProcessors[i].join()

if __name__ == "__main__":
    vm = VM()
    vm.run()
