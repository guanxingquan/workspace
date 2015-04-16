'''
Created on 2015-4-13

@author: guanxingquan
'''
from CoreServices import DeviceManagementService

class TestModel(object):
    '''
    Test about Device Model function
    '''

    def __init__(self):
        '''
        
        '''
        self.deviceManage = DeviceManagementService()
        
    
    def testcase1_getDeviceModel(self):
        self.deviceManage.listModels()