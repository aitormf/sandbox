# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.4
#
# <auto-generated>
#
# Generated from file `camera.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import image_ice

# Included module jderobot
_M_jderobot = Ice.openModule('jderobot')

# Start of module jderobot
__name__ = 'jderobot'

if 'CameraDescription' not in _M_jderobot.__dict__:
    _M_jderobot.CameraDescription = Ice.createTempClass()
    class CameraDescription(Ice.Object):
        """
        Static description of a camera
        """
        def __init__(self, name='', shortDescription='', streamingUri='', fdistx=0.0, fdisty=0.0, u0=0.0, v0=0.0, skew=0.0, posx=0.0, posy=0.0, posz=0.0, foax=0.0, foay=0.0, foaz=0.0, roll=0.0):
            self.name = name
            self.shortDescription = shortDescription
            self.streamingUri = streamingUri
            self.fdistx = fdistx
            self.fdisty = fdisty
            self.u0 = u0
            self.v0 = v0
            self.skew = skew
            self.posx = posx
            self.posy = posy
            self.posz = posz
            self.foax = foax
            self.foay = foay
            self.foaz = foaz
            self.roll = roll

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::CameraDescription')

        def ice_id(self, current=None):
            return '::jderobot::CameraDescription'

        def ice_staticId():
            return '::jderobot::CameraDescription'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_CameraDescription)

        __repr__ = __str__

    _M_jderobot.CameraDescriptionPrx = Ice.createTempClass()
    class CameraDescriptionPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.CameraDescriptionPrx.ice_checkedCast(proxy, '::jderobot::CameraDescription', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.CameraDescriptionPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::CameraDescription'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_CameraDescriptionPrx = IcePy.defineProxy('::jderobot::CameraDescription', CameraDescriptionPrx)

    _M_jderobot._t_CameraDescription = IcePy.defineClass('::jderobot::CameraDescription', CameraDescription, -1, (), False, False, None, (), (
        ('name', (), IcePy._t_string, False, 0),
        ('shortDescription', (), IcePy._t_string, False, 0),
        ('streamingUri', (), IcePy._t_string, False, 0),
        ('fdistx', (), IcePy._t_float, False, 0),
        ('fdisty', (), IcePy._t_float, False, 0),
        ('u0', (), IcePy._t_float, False, 0),
        ('v0', (), IcePy._t_float, False, 0),
        ('skew', (), IcePy._t_float, False, 0),
        ('posx', (), IcePy._t_float, False, 0),
        ('posy', (), IcePy._t_float, False, 0),
        ('posz', (), IcePy._t_float, False, 0),
        ('foax', (), IcePy._t_float, False, 0),
        ('foay', (), IcePy._t_float, False, 0),
        ('foaz', (), IcePy._t_float, False, 0),
        ('roll', (), IcePy._t_float, False, 0)
    ))
    CameraDescription._ice_type = _M_jderobot._t_CameraDescription

    _M_jderobot.CameraDescription = CameraDescription
    del CameraDescription

    _M_jderobot.CameraDescriptionPrx = CameraDescriptionPrx
    del CameraDescriptionPrx

if 'Camera' not in _M_jderobot.__dict__:
    _M_jderobot.Camera = Ice.createTempClass()
    class Camera(_M_jderobot.ImageProvider):
        """
        Camera interface
        """
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.Camera:
                raise RuntimeError('jderobot.Camera is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::Camera', '::jderobot::ImageProvider')

        def ice_id(self, current=None):
            return '::jderobot::Camera'

        def ice_staticId():
            return '::jderobot::Camera'
        ice_staticId = staticmethod(ice_staticId)

        def getCameraDescription(self, current=None):
            pass

        def setCameraDescription(self, description, current=None):
            pass

        def startCameraStreaming(self, current=None):
            pass

        def stopCameraStreaming(self, current=None):
            pass

        def reset(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_Camera)

        __repr__ = __str__

    _M_jderobot.CameraPrx = Ice.createTempClass()
    class CameraPrx(_M_jderobot.ImageProviderPrx):

        def getCameraDescription(self, _ctx=None):
            return _M_jderobot.Camera._op_getCameraDescription.invoke(self, ((), _ctx))

        def begin_getCameraDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Camera._op_getCameraDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getCameraDescription(self, _r):
            return _M_jderobot.Camera._op_getCameraDescription.end(self, _r)

        def setCameraDescription(self, description, _ctx=None):
            return _M_jderobot.Camera._op_setCameraDescription.invoke(self, ((description, ), _ctx))

        def begin_setCameraDescription(self, description, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Camera._op_setCameraDescription.begin(self, ((description, ), _response, _ex, _sent, _ctx))

        def end_setCameraDescription(self, _r):
            return _M_jderobot.Camera._op_setCameraDescription.end(self, _r)

        def startCameraStreaming(self, _ctx=None):
            return _M_jderobot.Camera._op_startCameraStreaming.invoke(self, ((), _ctx))

        def begin_startCameraStreaming(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Camera._op_startCameraStreaming.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_startCameraStreaming(self, _r):
            return _M_jderobot.Camera._op_startCameraStreaming.end(self, _r)

        def stopCameraStreaming(self, _ctx=None):
            return _M_jderobot.Camera._op_stopCameraStreaming.invoke(self, ((), _ctx))

        def begin_stopCameraStreaming(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Camera._op_stopCameraStreaming.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_stopCameraStreaming(self, _r):
            return _M_jderobot.Camera._op_stopCameraStreaming.end(self, _r)

        def reset(self, _ctx=None):
            return _M_jderobot.Camera._op_reset.invoke(self, ((), _ctx))

        def begin_reset(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.Camera._op_reset.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_reset(self, _r):
            return _M_jderobot.Camera._op_reset.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.CameraPrx.ice_checkedCast(proxy, '::jderobot::Camera', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.CameraPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::Camera'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_CameraPrx = IcePy.defineProxy('::jderobot::Camera', CameraPrx)

    _M_jderobot._t_Camera = IcePy.defineClass('::jderobot::Camera', Camera, -1, (), True, False, None, (_M_jderobot._t_ImageProvider,), ())
    Camera._ice_type = _M_jderobot._t_Camera

    Camera._op_getCameraDescription = IcePy.Operation('getCameraDescription', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_jderobot._t_CameraDescription, False, 0), ())
    Camera._op_setCameraDescription = IcePy.Operation('setCameraDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_jderobot._t_CameraDescription, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    Camera._op_startCameraStreaming = IcePy.Operation('startCameraStreaming', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_string, False, 0), ())
    Camera._op_stopCameraStreaming = IcePy.Operation('stopCameraStreaming', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Camera._op_reset = IcePy.Operation('reset', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_jderobot.Camera = Camera
    del Camera

    _M_jderobot.CameraPrx = CameraPrx
    del CameraPrx

if 'SetterCamera' not in _M_jderobot.__dict__:
    _M_jderobot.SetterCamera = Ice.createTempClass()
    class SetterCamera(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_jderobot.SetterCamera:
                raise RuntimeError('jderobot.SetterCamera is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::jderobot::SetterCamera')

        def ice_id(self, current=None):
            return '::jderobot::SetterCamera'

        def ice_staticId():
            return '::jderobot::SetterCamera'
        ice_staticId = staticmethod(ice_staticId)

        def setCamera(self, proxy, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_jderobot._t_SetterCamera)

        __repr__ = __str__

    _M_jderobot.SetterCameraPrx = Ice.createTempClass()
    class SetterCameraPrx(Ice.ObjectPrx):

        def setCamera(self, proxy, _ctx=None):
            return _M_jderobot.SetterCamera._op_setCamera.invoke(self, ((proxy, ), _ctx))

        def begin_setCamera(self, proxy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_jderobot.SetterCamera._op_setCamera.begin(self, ((proxy, ), _response, _ex, _sent, _ctx))

        def end_setCamera(self, _r):
            return _M_jderobot.SetterCamera._op_setCamera.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_jderobot.SetterCameraPrx.ice_checkedCast(proxy, '::jderobot::SetterCamera', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_jderobot.SetterCameraPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::jderobot::SetterCamera'
        ice_staticId = staticmethod(ice_staticId)

    _M_jderobot._t_SetterCameraPrx = IcePy.defineProxy('::jderobot::SetterCamera', SetterCameraPrx)

    _M_jderobot._t_SetterCamera = IcePy.defineClass('::jderobot::SetterCamera', SetterCamera, -1, (), True, False, None, (), ())
    SetterCamera._ice_type = _M_jderobot._t_SetterCamera

    SetterCamera._op_setCamera = IcePy.Operation('setCamera', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_jderobot._t_CameraPrx, False, 0),), (), None, ())

    _M_jderobot.SetterCamera = SetterCamera
    del SetterCamera

    _M_jderobot.SetterCameraPrx = SetterCameraPrx
    del SetterCameraPrx

# End of module jderobot
