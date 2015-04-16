'''
Created on 2015-4-10

@author: guanxingquan
'''
from arbiter.TestDeviceManagementServer import DeviceManagementServer
from arbiter.TestMysqlDataVerifier import MysqlDataVerifier
from arbiter.TestStreamControlServer import StreamControlServerClient
from arbiter.TestConfigControlService import ConfigControlServiceClient
from arbiter.TestDeviceDataReceiverService import DeviceDataReceiverServiceClient
#from arbiter.TestRecordingServerService import RecordingServerServiceClient
# from arbiter.TestDeviceServerService import DeviceServerServiceClient
from arbiter.TestDeviceControlService import DeviceControlServiceClient
# from arbiter.utils.ConfigurationReader import Config
# from arbiter.utils.Constants import addDevice
import logging
# import time

log = logging.getLogger("TestDemoB")

class TestDemoB(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.dms = DeviceManagementServer()
        self.dataVerifier = MysqlDataVerifier()
        self.scs = StreamControlServerClient()
        self.ccs = ConfigControlServiceClient()
        self.drs = DeviceDataReceiverServiceClient()
        self.dcs = DeviceControlServiceClient()
        #self.initConfigFile()
        #self.initCamera()
        assert True
    
    def testcase_deleteCamera(self):
        delDeviceRes = self.dms.testDeleteDevice()
        assert delDeviceRes
        isSuccess = self.dataVerifier.testIfDeviceDeleted()
        assert isSuccess
        pass
    
    