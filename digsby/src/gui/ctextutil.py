# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

import _ctextutil
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import wx._core
import wx._gdi
import wx 
__docfilter__ = wx._core.__DocFilter(globals()) 

def Subtract(*args, **kwargs):
  """Subtract(Rect r, int left=0, int right=0, int up=0, int down=0)"""
  return _ctextutil.Subtract(*args, **kwargs)

def RectPos(*args, **kwargs):
  """RectPos(Rect rect, Point point) -> PyObject"""
  return _ctextutil.RectPos(*args, **kwargs)

def truncateText(*args, **kwargs):
  """
    truncateText(String text, int size, Font font=None, DC dc=None, 
        String thepostfix=wxT("...")) -> String
    """
  return _ctextutil.truncateText(*args, **kwargs)


