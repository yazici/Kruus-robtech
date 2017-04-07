# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mouse_reader/Mouse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Mouse(genpy.Message):
  _md5sum = "8d3171768b3aa775674c4585e9dc2c0b"
  _type = "mouse_reader/Mouse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Key code as defined in linux/inupt.h
int16 x_movement
int16 y_movement

# Key name string as defined in evtest, see http://elinux.org/images/9/93/Evtest.c
string key_name

# 'True' if key was pressed, 'False' otherwise
bool key_pressed
"""
  __slots__ = ['x_movement','y_movement','key_name','key_pressed']
  _slot_types = ['int16','int16','string','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_movement,y_movement,key_name,key_pressed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Mouse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x_movement is None:
        self.x_movement = 0
      if self.y_movement is None:
        self.y_movement = 0
      if self.key_name is None:
        self.key_name = ''
      if self.key_pressed is None:
        self.key_pressed = False
    else:
      self.x_movement = 0
      self.y_movement = 0
      self.key_name = ''
      self.key_pressed = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2h.pack(_x.x_movement, _x.y_movement))
      _x = self.key_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.key_pressed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.x_movement, _x.y_movement,) = _struct_2h.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.key_name = str[start:end].decode('utf-8')
      else:
        self.key_name = str[start:end]
      start = end
      end += 1
      (self.key_pressed,) = _struct_B.unpack(str[start:end])
      self.key_pressed = bool(self.key_pressed)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2h.pack(_x.x_movement, _x.y_movement))
      _x = self.key_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.key_pressed))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 4
      (_x.x_movement, _x.y_movement,) = _struct_2h.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.key_name = str[start:end].decode('utf-8')
      else:
        self.key_name = str[start:end]
      start = end
      end += 1
      (self.key_pressed,) = _struct_B.unpack(str[start:end])
      self.key_pressed = bool(self.key_pressed)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_2h = struct.Struct("<2h")