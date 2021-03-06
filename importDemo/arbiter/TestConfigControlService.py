# -*- coding: GBK -*-
'''
 Created on 2014-7-16

@author: guanxingquan
'''

from CoreServices import ConfigControlService
from arbiter.utils.ConfigurationReader import Config
from arbiter.utils import ThriftClient
from arbiter.utils.Constants import arbiter,configControl,deleteDevice
import logging

log = logging.getLogger('testConfigControlService')
class ConfigControlServiceClient():
    client = None 
    def __init__(self):
        try:
            host = Config().getFromConfigs(arbiter, "arbiter-server-host")
            port = Config().getFromConfigs(arbiter, "config-control-server-port")
            self.client = ThriftClient.getThriftClient(host, port, ConfigControlService)
        except Exception, e:
            log.error("ConfigControlService init error:%s",e)
            raise Exception("ConfigControlService Exception")
    
    def tearDown(self):
        ThriftClient.closeThriftClient()
    
    def testSetCloudServer(self):
        try:
            kupHost = Config().getFromConfigs(configControl,"kup-arbiter-host")
            result = self.client.setCloudServer(kupHost)
            log.debug("result:%s",result)
            return result
        except Exception,e:
            log.error("Set Cloud Server found an error: %s ",e)
#             return False

    def testSetChunkSize(self):
        '''
          make sure setChunkSize() is success function
        '''
        try:
            log.debug('test setChunkSize')
            size = Config().getFromConfigs(configControl,"chunk-size")
#             print size
            result = self.client.setChunkSize((int)(size))
#             print result
            if result:
                log.debug('this function set chunk-size is success!')
            else:
                log.debug('the test have error~~')
            return result
        except Exception,e:
            log.error("testSetChunkSize error:%s",e)
            return False
#             raise Exception("testSetChunkSize exception")
    def testSetStreamLimit(self,size):
        try:
            deviceId = Config().getFromConfigs(deleteDevice,"device-id")
            result = self.client.setStreamStorageLimit(deviceId,"0",size)
            log.debug('testSetStreamLimit result : %s',result)
            return result
        except Exception,e:
            log.error('error : %s',e)
            return None
                    