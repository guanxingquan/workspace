'''
Created on 2015-04-07

@author: guanxingquan
'''
from arbiter.TestDeviceManagementServer import DeviceManagementServer
from arbiter.TestMysqlDataVerifier import MysqlDataVerifier
from arbiter.TestStreamControlServer import StreamControlServerClient
from arbiter.TestConfigControlService import ConfigControlServiceClient
from arbiter.TestDeviceDataReceiverService import DeviceDataReceiverServiceClient
from arbiter.TestRecordingServerService import RecordingServerServiceClient
from arbiter.TestDeviceServerService import DeviceServerServiceClient
from arbiter.TestDeviceControlService import DeviceControlServiceClient
# from arbiter.utils.ConfigurationReader import Config
# from arbiter.utils.Constants import addDevice
import logging
import time

log = logging.getLogger("TestNose")


class TestNose(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        init all server
        '''
        self.dms = DeviceManagementServer()
        self.dataVerifier = MysqlDataVerifier()
        self.scs = StreamControlServerClient()
        self.ccs = ConfigControlServiceClient()
        self.drs = DeviceDataReceiverServiceClient()
        self.dcs = DeviceControlServiceClient()
        self.dss = DeviceServerServiceClient()
        self.rss = RecordingServerServiceClient()
#         self.initConfigFile()
        assert True
    
    def testcase1_setKAIUP(self):
        '''
        Test Set KAIUP Server
        '''
        result = self.ccs.testSetCloudServer()
        assert result
        dbResult = self.dataVerifier.testConfigurationsHavKUP()
        assert dbResult
    

    
    def testcase2_onlineDeviceLiveview(self):
        '''
        Test Camera Live View
        1. URL
        2. Frame Rate
        '''
        urlResult = self.scs.testLiveViewResultUrl()
        assert urlResult
        
        addResult = self.dataVerifier.testIfAddedToStreamSessionInfo()
        assert addResult
        
        delResult = self.dataVerifier.testIfDelFromStreamSessionInfo()
        assert delResult
        
        rateResult = self.dss.testDeviceFrameRate()
        assert rateResult
        pass

    
    def testcase3_keepSession(self):
        '''
        Test Keep Session
        '''
        sessionResult = self.scs.controlSession()
        assert sessionResult    
        pass
    
    def testcase4_setChunkSize(self):
        '''
        Test Set Chunk Size
        '''
        result = self.ccs.testSetChunkSize()
        assert result
        pass
    
    def testcase5_streamStorageLimitZero(self):
        '''
        Test Stream Storage Limit Zero
        '''
#         global self.rss
#         self.rss = RecordingServerServiceClient()
        recordResult = self.dms.beginVideoRecording()
        assert recordResult
        begin_local_time = time.strftime("%d%m%Y%H%M%S",time.localtime(time.time()))
        log.debug('begin_local_time : %s',begin_local_time)
        time.sleep(40)
        result = self.streamStorageLimitStrategy(0, 120, 180, begin_local_time,0)
        assert result
    
    def testcase6_streamStorageLimitOther(self):
        '''
        Test Stream Storage Limit 10M and 30M 
        '''
        recordResult = self.dms.beginVideoRecording()
        assert recordResult
        begin_local_time = time.strftime("%d%m%Y%H%M%S",time.localtime(time.time()))
        log.debug('begin_local_time : %s',begin_local_time)
        time.sleep(40)
        log.debug('message: next will wait time 130s for test 10M')
        one_result = self.streamStorageLimitStrategy(10, 130, 210, begin_local_time,1)
        assert one_result
        log.debug('message:next will wait time  150s for test 30M')
        two_result = self.streamStorageLimitStrategy(30, 0, 150, begin_local_time,2)
        assert two_result
    
    def testcase7_videoStore(self):
        '''
        Test Video Storage
        '''
        result = self.dms.TestVideoStrategy()
        assert result
        
        time.sleep(15)
        
        videoUrlOK = self.scs.checkVideoListSize()
        assert videoUrlOK
        
        videoContentOK = self.rss.testGetVideoStreamList()
        assert videoContentOK
        
        pass
    
    def testcase8_imageStore(self):
        '''
        Test Image Storage
        '''
        result = self.dms.testPhotoStrategy()
        assert result
        imageUrlOK = self.scs.checkPhotoUrlSize()
        assert imageUrlOK
        imageContentOK = self.rss.testGetPhotoStreamList()
        assert imageContentOK
        pass

        
    def testcase9_VideoEvent(self):
        '''
        Test video-event
        will cycles 6 time ,if success time >= 5 ,assert True
        '''
        isTrue = True
        cycles_num = 0
        succ_time = 0
        upres = self.dms.beginVideoRecording()
        if upres:
            time.sleep(40)
        while isTrue:
            cycles_num += 1
            log.info('[%d] the %d round event video recording...', cycles_num, cycles_num)
            result = self.drs.sendEventToArbiter()
            if result:
                log.info("send event video to Arbiter             OK")
                time.sleep(10)
                eventContentOK = self.rss.testGetEventStreamList()
                if eventContentOK:
                    log.info("event video content check               OK")
                    succ_time += 1
                else:
                    log.info("event video content check               False")
            else:
                log.info("send event video to Arbiter             False")
            
            if cycles_num == 6:
                isTrue = False
                print succ_time
                assert succ_time >= 5

        
    def updateDevice(self):
        upDeviceRes = self.dms.testUpdateDevice()
        assert upDeviceRes
        pass
        
    
    def streamStorageLimitStrategy(self,size,onesleeptime,twosleeptime,begin_local_time,number):
        result = self.ccs.testSetStreamLimit(size)
        log.debug('set stream list size, result=%s', result)
        if result:
            log.info('set storage space is %dM                OK',size)
            time.sleep(onesleeptime)
            end_local_time = time.strftime("%d%m%Y%H%M%S",time.localtime(time.time()))
            log.debug('end_local_time : %s',end_local_time)
            if size == 0:
                if self.dms.stopVideoRecording():
#                     log.debug('close video time :')
                    time.sleep(twosleeptime)
                    log.debug('RecordingServerService : %s',self.rss)
                    if self.rss is None:
                        raise Exception("RecordingServerService NoneType")
                    zero_first_video_begin = self.rss.getVideoStreamList_FirstValue(begin_local_time,end_local_time)
                    if zero_first_video_begin is None:
                        log.info('test storage space is 0M                OK')
                        return True
                    else:
                        log.info('test storage space is 0M                False')
                        return False
                else:
                    return False
             
            #get the first video before RS cleaned the videos
            first_video_begin = self.rss.getVideoStreamList_FirstValue(begin_local_time,end_local_time)
            log.debug('first_video_begin :%s',first_video_begin)
            time.sleep(twosleeptime)
            
            #get the first video after RS cleans the videos
            end_local_time = time.strftime("%d%m%Y%H%M%S",time.localtime(time.time()))
            second_video_begin = self.rss.getVideoStreamList_FirstValue(begin_local_time,end_local_time)
            log.debug('second_video_begin : %s',second_video_begin)
            
            #compare the first video before and after RS cleaned, verify if the result is correct 
            if number == 1 and first_video_begin != second_video_begin:
                log.info('test storage space is %sM                OK',size)
                return True
            elif number == 1 and first_video_begin == second_video_begin:
                log.info('test storage space is %sM                False',size)
                return False
            
            if number == 2 and first_video_begin == second_video_begin:
                log.info('test storage space is %sM                OK',size)
                self.dms.stopVideoRecording()
                return True
            elif number == 2 and first_video_begin != second_video_begin:
                log.info('test storage space is %sM                False',size)
                return False
        else:
            log.info('set storage space is %dM                 False',size)
            return False

    
    def deleteDeviceAndCleanData(self):
        try:
            DeviceManagementServer().testDeleteDevice()
        except Exception,e:
            log.error("exception,%s", e)
            self.deleteDeviceAndCleanData()
        #clean device data
        dataVerifier = MysqlDataVerifier()
        dataVerifier.cleanDeviceInfo()
        
        pass
    