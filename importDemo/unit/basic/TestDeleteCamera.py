'''
Created on 2015-04-14

@author: guanxingquan
'''
from arbiter.TestDeviceManagementServer import DeviceManagementServer
from arbiter.TestMysqlDataVerifier import MysqlDataVerifier
from arbiter.utils.ConfigurationReader import Config
from arbiter.utils.Constants import commonConfige
from arbiter.utils.Constants import deviceModelA
import time

class TestDeleteCamera(object):
    '''
    Test delete Camera
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
        result = self.deviceManage.testAddDevice(deviceModelA)
        assert result
        inresult = self.mysqlData.testCorrectnessInDevices()
        assert inresult
        time.sleep(5)
    
    def tearDown(self):
        '''
        The end:
            need to clear test data when test end
        '''
        self.mysqlData.cleanDeviceInfo()
    
    def testcase_DeleteCamera(self):
        '''
        Test Delete Camera
        '''
        result = self.deviceManage.testDeleteDevice()
        assert result
        
        deleteResu = self.mysqlData.testIfDeviceDeleted()
        assert deleteResu
        
        pass
    
    
    
    