from common.utils import CBCLogger
from common.utils import RetCode

import sys, os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from executor.executor import Executor

import subprocess

class ClusterExecutor(Executor):
    def __init__(self):
        pass

class CephExecutor(ClusterExecutor):
    def __init__(self, config_obj):
        self.config_obj = config_obj

    def build(self):
        CBCLogger.info("Build Ceph source code.")
        return RetCode.OK

    def setup(self):
        CBCLogger.info("Setup and deploy Ceph cluster.")
        #CBCLogger.debug("Download cephadm utility.")
        #ret = subprocess.call("curl --silent --remote-name --location https://github.com/ceph/ceph/raw/octopus/src/cephadm/cephadm", shell=True)
        #if ret != 0:
        #    CBCLogger.error("Download cephadm utility failed.")
        #    return RetCode.Error
        #CBCLogger.debug("Chmod cephadm utility.")
        #subprocess.call("chmod +x ./cephadm", shell=True)

    def run(self):
        CBCLogger.info("Deploy Ceph cluster.")
        CBCLogger.debug("(optional) Add ceph repo.")
        ret = subprocess.call("cephadm add-repo --release octopus", shell=True)
        if ret != 0:
            CBCLogger.error("(optional) Add ceph repo failed.")
            return RetCode.Error
        CBCLogger.debug("Bootstrap cephadm monitor.")
        ret = subprocess.call("cephadm bootstrap --mon-ip 10.239.241.85", shell=True)
        if ret != 0:
            CBCLogger.error("Bootstrap cephadm monitor failed.")
            return RetCode.Error

        CBCLogger.debug("Ceph orch add vol1.")
        ret = subprocess.call("cephadm shell -- ceph orch daemon add osd ceph8:ceph_volumes/vol1", shell=True)
        if ret != 0:
            CBCLogger.error("Ceph orch add vol1 failed.")
            return RetCode.Error
        CBCLogger.debug("Ceph orch add vol2.")
        ret = subprocess.call("cephadm shell -- ceph orch daemon add osd ceph8:ceph_volumes/vol2", shell=True)
        if ret != 0:
            CBCLogger.error("Ceph orch add vol1 failed.")
            return RetCode.Error
        CBCLogger.debug("Ceph orch add vol3.")
        ret = subprocess.call("cephadm shell -- ceph orch daemon add osd ceph8:ceph_volumes/vol3", shell=True)
        if ret != 0:
            CBCLogger.error("Ceph orch add vol1 failed.")
            return RetCode.Error
        CBCLogger.debug("Ceph orch add vol4.")
        ret = subprocess.call("cephadm shell -- ceph orch daemon add osd ceph8:ceph_volumes/vol4", shell=True)
        if ret != 0:
            CBCLogger.error("Ceph orch add vol1 failed.")
            return RetCode.Error
        return RetCode.OK

    def cleanup(self):
        CBCLogger.info("Clean up the cluster.")
        return RetCode.OK

