'''
Created on 2015-4-10

@author: guanxingquan
'''

from arbiter.TestDeviceManagementServer import DeviceManagementServer
from arbiter.TestMysqlDataVerifier import MysqlDataVerifier
from arbiter.TestDeviceServerService import DeviceServerServiceClient
from arbiter.utils.ConfigurationReader import Config
from arbiter.utils.Constants import onlineDevice
import logging
import time

log = logging.getLogger("operation")
def setUp():
    '''
    Init a online camera to continue other test
    '''
    try:
        initConfigFile()
        result = DeviceManagementServer().testAddDevice(onlineDevice)
        assert result
        
        isInDevices = MysqlDataVerifier().testCorrectnessInDevices()
        assert isInDevices
        
        isInDsDevInfo = MysqlDataVerifier().testCorrectnessInDsDeviceInfo()
        assert isInDsDevInfo
        
        isAddedToDS = MysqlDataVerifier().testIfDeviceAddedToDs()
        assert isAddedToDS
    
        time.sleep(3)
    
        isInDS = DeviceServerServiceClient().testDeviceisinDs()
        assert isInDS
        
    except Exception,e:
        log.error("operation SetUp Error: %s ",e)
        tearDown()


def tearDown():
    '''
    used to clear camera data when test over
    '''
    delDeviceRes = DeviceManagementServer().testDeleteDevice()
    assert delDeviceRes
    MysqlDataVerifier().cleanDeviceInfo()
    isSuccess = MysqlDataVerifier().testIfDeviceDeleted()
    assert isSuccess
    pass

def initConfigFile():
    '''
    Sometimes when the last-round testing failed because of exceptions, the parameter values
    in configuration.cfg will not be changed to the initial value, and this may cause problems.
    E.g., if cloud-recording-enabled is true when exception happened, it will affect the next round testing.
         
    So we should reset some of the import parameters in configuration.cfg before each testing. 
    '''
    Config().writeToConfig(onlineDevice, "snapshot-recording-enabled", "false")
    Config().writeToConfig(onlineDevice, "cloud-recording-enabled", "false")