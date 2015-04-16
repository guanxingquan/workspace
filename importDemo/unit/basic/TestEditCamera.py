'''
Created on 2015-4-14

@author: guanxingquan
'''
from arbiter.TestDeviceManagementServer import DeviceManagementServer
from arbiter.TestMysqlDataVerifier import MysqlDataVerifier
from arbiter.utils.ConfigurationReader import Config
from arbiter.utils.Constants import commonConfige
from arbiter.utils.Constants import deviceModelA
import time

class TestEditCamera(object):
    '''
    Test Update Camera
    '''

    def __init__(self):
        '''
        Init some Service
        '''
        self.deviceManage = DeviceManagementServer()
        self.mysqlData = MysqlDataVerifier()
        
    def setUp(self):
        '''
        The premise:
            need a camera have in device server
        '''
        Config("device-information.cfg").writeToConfig(commonConfige, "snapshot-recording-enabled", "false")
        Config("device-information.cfg").writeToConfig(commonConfige, "cloud-recording-enabled", "false")
        self.deviceManage.testAddDevice(deviceModelA)
        result = self.mysqlData.testCorrectnessInDevices()
        assert result
        time.sleep(5)
    
    def tearDown(self):
        '''
        The end:
            need to clear test data when test end
        '''
        self.mysqlData.cleanDeviceInfo()
        
        
    def testcase_EditCamera(self):
        '''
        Test for Update
        '''
        result = self.deviceManage.testUpdateDevice()
        assert result
        updataResu = self.mysqlData.updataDeviceResult()
        assert updataResu
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    