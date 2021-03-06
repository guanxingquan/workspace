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
  EventService - this service provides API for event sources to push events to Platform.
  """
  def pushEvent(self, eventId, details):
    """
    Push an event to the Platform.

    (1) eventId - ID of the event
    (2) details - a structure with more details about this event


    Parameters:
     - eventId
     - details
    """
    pass


class Client(Iface):
  """
  EventService - this service provides API for event sources to push events to Platform.
  """
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def pushEvent(self, eventId, details):
    """
    Push an event to the Platform.

    (1) eventId - ID of the event
    (2) details - a structure with more details about this event


    Parameters:
     - eventId
     - details
    """
    self.send_pushEvent(eventId, details)
    return self.recv_pushEvent()

  def send_pushEvent(self, eventId, details):
    self._oprot.writeMessageBegin('pushEvent', TMessageType.CALL, self._seqid)
    args = pushEvent_args()
    args.eventId = eventId
    args.details = details
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_pushEvent(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = pushEvent_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.platformExp is not None:
      raise result.platformExp
    raise TApplicationException(TApplicationException.MISSING_RESULT, "pushEvent failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["pushEvent"] = Processor.process_pushEvent

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

  def process_pushEvent(self, seqid, iprot, oprot):
    args = pushEvent_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = pushEvent_result()
    try:
      result.success = self._handler.pushEvent(args.eventId, args.details)
    except PlatformException, platformExp:
      result.platformExp = platformExp
    oprot.writeMessageBegin("pushEvent", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class pushEvent_args:
  """
  Attributes:
   - eventId
   - details
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'eventId', None, None, ), # 1
    (2, TType.STRUCT, 'details', (EventStructures.ttypes.EventDetails, EventStructures.ttypes.EventDetails.thrift_spec), None, ), # 2
  )

  def __init__(self, eventId=None, details=None,):
    self.eventId = eventId
    self.details = details

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
          self.eventId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.details = EventStructures.ttypes.EventDetails()
          self.details.read(iprot)
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
    oprot.writeStructBegin('pushEvent_args')
    if self.eventId is not None:
      oprot.writeFieldBegin('eventId', TType.STRING, 1)
      oprot.writeString(self.eventId)
      oprot.writeFieldEnd()
    if self.details is not None:
      oprot.writeFieldBegin('details', TType.STRUCT, 2)
      self.details.write(oprot)
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

class pushEvent_result:
  """
  Attributes:
   - success
   - platformExp
  """

  thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'platformExp', (PlatformException, PlatformException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, platformExp=None,):
    self.success = success
    self.platformExp = platformExp

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
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.platformExp = PlatformException()
          self.platformExp.read(iprot)
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
    oprot.writeStructBegin('pushEvent_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 0)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    if self.platformExp is not None:
      oprot.writeFieldBegin('platformExp', TType.STRUCT, 1)
      self.platformExp.write(oprot)
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
