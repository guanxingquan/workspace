'''
Created on 2015-4-10
@author: kaisquare

Edit on 2015-4-14
@author: guanxingquan

'''
from arbiter.TestDeviceManagementServer import DeviceManagementServer
from arbiter.TestMysqlDataVerifier import MysqlDataVerifier
from arbiter.utils.Constants import deviceModelA,deviceModelB,deviceModelC,deviceModelD
from arbiter.utils.ConfigurationReader import Config
from arbiter.utils.Constants import commonConfige

class TestAddOfflineCamera(object):
    '''
    Add a lot of Camera Model
    '''

    def __init__(self):
        '''
        init Server necessary
        '''
        self.dms = DeviceManagementServer()
        self.dataVerifier = MysqlDataVerifier()
        pass
    
    def setUp(self):
        Config("device-information.cfg").writeToConfig(commonConfige, "snapshot-recording-enabled", "false")
        Config("device-information.cfg").writeToConfig(commonConfige, "cloud-recording-enabled", "false")
        pass
    
    def tearDown(self):
        '''
        Clear Device Inforation
        '''
        self.dataVerifier.cleanDeviceInfo()
        pass
    
    def testcase_addCameraA(self):
        '''
        Add Camera ModelA
        '''
        result = self.dms.testAddDevice(deviceModelA)
        assert result
        isInDevices = self.dataVerifier.testCorrectnessInDevices()
        assert isInDevices
        
    def testcase_addCameraB(self):
        '''
        Add Camera ModelB
        '''
        result = self.dms.testAddDevice(deviceModelB)
        assert result
        isInDevices = self.dataVerifier.testCorrectnessInDevices()
        assert isInDevices
    
    def testcase_addCameraC(self):
        '''
        Add Camera ModelC
        '''
        result = self.dms.testAddDevice(deviceModelC)
        assert result
        isInDevices = self.dataVerifier.testCorrectnessInDevices()
        assert isInDevices
    
    def testcase_addCameraD(self):
        '''
        Add Camera ModelD
        '''
        result = self.dms.testAddDevice(deviceModelD)
        assert result
        isInDevices = self.dataVerifier.testCorrectnessInDevices()
        assert isInDevices
    
    