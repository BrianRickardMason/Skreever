import Processor

class VM(object):
    """VM class.
    
    Attributes:
        mProcessors: An array of processors.
    
    """
    
    def __init__(self):
        self.mProcessors = []
        for i in range(10):
            self.mProcessors.append(Processor.Processor("Processor" + str(i)))
            self.mProcessors[i].setDaemon(True)
            self.mProcessors[i].start()

    def run(self):
        for i in range(10):
            self.mProcessors[i].join()

if __name__ == "__main__":
    vm = VM()
    vm.run()
