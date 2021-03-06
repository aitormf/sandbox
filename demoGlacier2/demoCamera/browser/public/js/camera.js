// **********************************************************************
//
// Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.6.4
//
// <auto-generated>
//
// Generated from file `camera.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

(function(module, require, exports)
{
    var Ice = require("ice").Ice;
    var __M = Ice.__M;
    var jderobot = require("jderobot/image").jderobot;
    var Slice = Ice.Slice;

    /**
     * Static description of a camera
     **/
    jderobot.CameraDescription = Slice.defineObject(
        function(name, shortDescription, streamingUri, fdistx, fdisty, u0, v0, skew, posx, posy, posz, foax, foay, foaz, roll)
        {
            Ice.Object.call(this);
            this.name = name !== undefined ? name : "";
            this.shortDescription = shortDescription !== undefined ? shortDescription : "";
            this.streamingUri = streamingUri !== undefined ? streamingUri : "";
            this.fdistx = fdistx !== undefined ? fdistx : 0.0;
            this.fdisty = fdisty !== undefined ? fdisty : 0.0;
            this.u0 = u0 !== undefined ? u0 : 0.0;
            this.v0 = v0 !== undefined ? v0 : 0.0;
            this.skew = skew !== undefined ? skew : 0.0;
            this.posx = posx !== undefined ? posx : 0.0;
            this.posy = posy !== undefined ? posy : 0.0;
            this.posz = posz !== undefined ? posz : 0.0;
            this.foax = foax !== undefined ? foax : 0.0;
            this.foay = foay !== undefined ? foay : 0.0;
            this.foaz = foaz !== undefined ? foaz : 0.0;
            this.roll = roll !== undefined ? roll : 0.0;
        },
        Ice.Object, undefined, 1,
        [
            "::Ice::Object",
            "::jderobot::CameraDescription"
        ],
        -1,
        function(__os)
        {
            __os.writeString(this.name);
            __os.writeString(this.shortDescription);
            __os.writeString(this.streamingUri);
            __os.writeFloat(this.fdistx);
            __os.writeFloat(this.fdisty);
            __os.writeFloat(this.u0);
            __os.writeFloat(this.v0);
            __os.writeFloat(this.skew);
            __os.writeFloat(this.posx);
            __os.writeFloat(this.posy);
            __os.writeFloat(this.posz);
            __os.writeFloat(this.foax);
            __os.writeFloat(this.foay);
            __os.writeFloat(this.foaz);
            __os.writeFloat(this.roll);
        },
        function(__is)
        {
            this.name = __is.readString();
            this.shortDescription = __is.readString();
            this.streamingUri = __is.readString();
            this.fdistx = __is.readFloat();
            this.fdisty = __is.readFloat();
            this.u0 = __is.readFloat();
            this.v0 = __is.readFloat();
            this.skew = __is.readFloat();
            this.posx = __is.readFloat();
            this.posy = __is.readFloat();
            this.posz = __is.readFloat();
            this.foax = __is.readFloat();
            this.foay = __is.readFloat();
            this.foaz = __is.readFloat();
            this.roll = __is.readFloat();
        },
        false);

    jderobot.CameraDescriptionPrx = Slice.defineProxy(Ice.ObjectPrx, jderobot.CameraDescription.ice_staticId, undefined);

    Slice.defineOperations(jderobot.CameraDescription, jderobot.CameraDescriptionPrx);

    /**
     * Camera interface
     **/
    jderobot.Camera = Slice.defineObject(
        undefined,
        Ice.Object,
        [
            jderobot.ImageProvider
        ], 1,
        [
            "::Ice::Object",
            "::jderobot::Camera",
            "::jderobot::ImageProvider"
        ],
        -1, undefined, undefined, false);

    jderobot.CameraPrx = Slice.defineProxy(Ice.ObjectPrx, jderobot.Camera.ice_staticId, [
        jderobot.ImageProviderPrx]);

    Slice.defineOperations(jderobot.Camera, jderobot.CameraPrx,
    {
        "getCameraDescription": [, 2, 2, , , ["jderobot.CameraDescription", true], , , , , true],
        "setCameraDescription": [, , , , , [3], [["jderobot.CameraDescription", true]], , , true, ],
        "startCameraStreaming": [, , , , , [7], , , , , ],
        "stopCameraStreaming": [, , , , , , , , , , ],
        "reset": [, , , , , , , , , , ]
    });

    jderobot.SetterCamera = Slice.defineObject(
        undefined,
        Ice.Object, undefined, 1,
        [
            "::Ice::Object",
            "::jderobot::SetterCamera"
        ],
        -1, undefined, undefined, false);

    jderobot.SetterCameraPrx = Slice.defineProxy(Ice.ObjectPrx, jderobot.SetterCamera.ice_staticId, undefined);

    Slice.defineOperations(jderobot.SetterCamera, jderobot.SetterCameraPrx,
    {
        "setCamera": [, , , , , , [["jderobot.CameraPrx"]], , , , ]
    });
    exports.jderobot = jderobot;
}
(typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? module : undefined,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? require : this.Ice.__require,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? exports : this));
