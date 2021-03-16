import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from analyzer.analyzer import *
from common.utils import CBCLogger

class DataParser(Analyzer):
    def __init__(self):
        pass

    def build(self):
        CBCLogger.info("Build Parser source code.")

    def setup(self):
        CBCLogger.info("Setup Parser.")

    def run(self):
        CBCLogger.info("Run Parser.")
    
    def check_bottleneck(self):
        CBCLogger.info("Check bottleneck is in Ceph.")
        return True
