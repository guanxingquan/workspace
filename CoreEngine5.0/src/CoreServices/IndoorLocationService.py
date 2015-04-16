#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  """
  IndoorLocationService - Indoor location tracking service.
  """
  def getMaps(self, deviceId):
    """
    Get list of all maps associated with a controller.
    (1) deviceId - Device ID of the controller.
    Returns maps in system.

    Parameters:
     - deviceId
    """
    pass

  def getTags(self, deviceId):
    """
    Get list of all tags associated with a controller.
    (1) deviceId - Device ID of the controller.
    Returns tags in system.

    Parameters:
     - deviceId
    """
    pass

  def getTagLocation(self, deviceId, tagId, startTimestamp, endTimestamp):
    """
    Retrives list of locations of a tag during a specified time frame.

    (1) deviceId - Device ID of the controller
    (2) tagId - ID of the tag to locate
    (3) startTimestamp - start time, ddMMyyyyHHmmss format
    (4) endTimestamp - end time, ddMMyyyyHHmmss format

    Note: set startTimestamp and endTimestamp to null or "" to get last known location

    Parameters:
     - deviceId
     - tagId
     - startTimestamp
     - endTimestamp
    """
    pass


class Client(Iface):
  """
  IndoorLocationService - Indoor location tracking service.
  """
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def getMaps(self, deviceId):
    """
    Get list of all maps associated with a controller.
    (1) deviceId - Device ID of the controller.
    Returns maps in system.

    Parameters:
     - deviceId
    """
    self.send_getMaps(deviceId)
    return self.recv_getMaps()

  def send_getMaps(self, deviceId):
    self._oprot.writeMessageBegin('getMaps', TMessageType.CALL, self._seqid)
    args = getMaps_args()
    args.deviceId = deviceId
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getMaps(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getMaps_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.coreExp is not None:
      raise result.coreExp
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getMaps failed: unknown result");

  def getTags(self, deviceId):
    """
    Get list of all tags associated with a controller.
    (1) deviceId - Device ID of the controller.
    Returns tags in system.

    Parameters:
     - deviceId
    """
    self.send_getTags(deviceId)
    return self.recv_getTags()

  def send_getTags(self, deviceId):
    self._oprot.writeMessageBegin('getTags', TMessageType.CALL, self._seqid)
    args = getTags_args()
    args.deviceId = deviceId
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getTags(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getTags_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.coreExp is not None:
      raise result.coreExp
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getTags failed: unknown result");

  def getTagLocation(self, deviceId, tagId, startTimestamp, endTimestamp):
    """
    Retrives list of locations of a tag during a specified time frame.

    (1) deviceId - Device ID of the controller
    (2) tagId - ID of the tag to locate
    (3) startTimestamp - start time, ddMMyyyyHHmmss format
    (4) endTimestamp - end time, ddMMyyyyHHmmss format

    Note: set startTimestamp and endTimestamp to null or "" to get last known location

    Parameters:
     - deviceId
     - tagId
     - startTimestamp
     - endTimestamp
    """
    self.send_getTagLocation(deviceId, tagId, startTimestamp, endTimestamp)
    return self.recv_getTagLocation()

  def send_getTagLocation(self, deviceId, tagId, startTimestamp, endTimestamp):
    self._oprot.writeMessageBegin('getTagLocation', TMessageType.CALL, self._seqid)
    args = getTagLocation_args()
    args.deviceId = deviceId
    args.tagId = tagId
    args.startTimestamp = startTimestamp
    args.endTimestamp = endTimestamp
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getTagLocation(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = getTagLocation_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.coreExp is not None:
      raise result.coreExp
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getTagLocation failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["getMaps"] = Processor.process_getMaps
    self._processMap["getTags"] = Processor.process_getTags
    self._processMap["getTagLocation"] = Processor.process_getTagLocation

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_getMaps(self, seqid, iprot, oprot):
    args = getMaps_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getMaps_result()
    try:
      result.success = self._handler.getMaps(args.deviceId)
    except CoreException, coreExp:
      result.coreExp = coreExp
    oprot.writeMessageBegin("getMaps", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getTags(self, seqid, iprot, oprot):
    args = getTags_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getTags_result()
    try:
      result.success = self._handler.getTags(args.deviceId)
    except CoreException, coreExp:
      result.coreExp = coreExp
    oprot.writeMessageBegin("getTags", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getTagLocation(self, seqid, iprot, oprot):
    args = getTagLocation_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getTagLocation_result()
    try:
      result.success = self._handler.getTagLocation(args.deviceId, args.tagId, args.startTimestamp, args.endTimestamp)
    except CoreException, coreExp:
      result.coreExp = coreExp
    oprot.writeMessageBegin("getTagLocation", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class getMaps_args:
  """
  Attributes:
   - deviceId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'deviceId', None, None, ), # 1
  )

  def __init__(self, deviceId=None,):
    self.deviceId = deviceId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.deviceId = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getMaps_args')
    if self.deviceId is not None:
      oprot.writeFieldBegin('deviceId', TType.STRING, 1)
      oprot.writeString(self.deviceId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getMaps_result:
  """
  Attributes:
   - success
   - coreExp
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(IndoorMapInfo, IndoorMapInfo.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'coreExp', (CoreException, CoreException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, coreExp=None,):
    self.success = success
    self.coreExp = coreExp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype108, _size105) = iprot.readListBegin()
          for _i109 in xrange(_size105):
            _elem110 = IndoorMapInfo()
            _elem110.read(iprot)
            self.success.append(_elem110)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.coreExp = CoreException()
          self.coreExp.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getMaps_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter111 in self.success:
        iter111.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.coreExp is not None:
      oprot.writeFieldBegin('coreExp', TType.STRUCT, 1)
      self.coreExp.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getTags_args:
  """
  Attributes:
   - deviceId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'deviceId', None, None, ), # 1
  )

  def __init__(self, deviceId=None,):
    self.deviceId = deviceId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.deviceId = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getTags_args')
    if self.deviceId is not None:
      oprot.writeFieldBegin('deviceId', TType.STRING, 1)
      oprot.writeString(self.deviceId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getTags_result:
  """
  Attributes:
   - success
   - coreExp
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(TagInfo, TagInfo.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'coreExp', (CoreException, CoreException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, coreExp=None,):
    self.success = success
    self.coreExp = coreExp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype115, _size112) = iprot.readListBegin()
          for _i116 in xrange(_size112):
            _elem117 = TagInfo()
            _elem117.read(iprot)
            self.success.append(_elem117)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.coreExp = CoreException()
          self.coreExp.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getTags_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter118 in self.success:
        iter118.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.coreExp is not None:
      oprot.writeFieldBegin('coreExp', TType.STRUCT, 1)
      self.coreExp.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getTagLocation_args:
  """
  Attributes:
   - deviceId
   - tagId
   - startTimestamp
   - endTimestamp
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'deviceId', None, None, ), # 1
    (2, TType.STRING, 'tagId', None, None, ), # 2
    (3, TType.STRING, 'startTimestamp', None, None, ), # 3
    (4, TType.STRING, 'endTimestamp', None, None, ), # 4
  )

  def __init__(self, deviceId=None, tagId=None, startTimestamp=None, endTimestamp=None,):
    self.deviceId = deviceId
    self.tagId = tagId
    self.startTimestamp = startTimestamp
    self.endTimestamp = endTimestamp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.deviceId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.tagId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.startTimestamp = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.endTimestamp = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getTagLocation_args')
    if self.deviceId is not None:
      oprot.writeFieldBegin('deviceId', TType.STRING, 1)
      oprot.writeString(self.deviceId)
      oprot.writeFieldEnd()
    if self.tagId is not None:
      oprot.writeFieldBegin('tagId', TType.STRING, 2)
      oprot.writeString(self.tagId)
      oprot.writeFieldEnd()
    if self.startTimestamp is not None:
      oprot.writeFieldBegin('startTimestamp', TType.STRING, 3)
      oprot.writeString(self.startTimestamp)
      oprot.writeFieldEnd()
    if self.endTimestamp is not None:
      oprot.writeFieldBegin('endTimestamp', TType.STRING, 4)
      oprot.writeString(self.endTimestamp)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getTagLocation_result:
  """
  Attributes:
   - success
   - coreExp
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(IndoorLocationInfo, IndoorLocationInfo.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'coreExp', (CoreException, CoreException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, coreExp=None,):
    self.success = success
    self.coreExp = coreExp

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype122, _size119) = iprot.readListBegin()
          for _i123 in xrange(_size119):
            _elem124 = IndoorLocationInfo()
            _elem124.read(iprot)
            self.success.append(_elem124)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.coreExp = CoreException()
          self.coreExp.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getTagLocation_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter125 in self.success:
        iter125.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.coreExp is not None:
      oprot.writeFieldBegin('coreExp', TType.STRUCT, 1)
      self.coreExp.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
