from common.utils import CBCLogger

import sys, os
import threading
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from executor.executor import Executor

class ToolExecutor(Executor):
    def __init__(self):
        pass

class DstatExecutor(ToolExecutor):
    def __init__(self, config_obj):
        self.config_obj = config_obj
        self.runner = DstatThread()

    def build(self):
        CBCLogger.info("Build Dstat source code.")
    
    def setup(self):
        CBCLogger.info("Setup Dstat.")
    
    def run(self):
        self.runner.start()
        #self.runner.join()

class DstatThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        CBCLogger.info("Run Dstat in another thread.")
        CBCLogger.info("Run Dstat Start.")
        time.sleep(10)
        CBCLogger.info("Run Dstat End.")
