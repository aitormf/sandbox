// **********************************************************************
//
// Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.6.3
//
// <auto-generated>
//
// Generated from file `motors.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

(function(module, require, exports)
{
    var Ice = require("ice").Ice;
    var __M = Ice.__M;
    var Slice = Ice.Slice;

    var jderobot = __M.module("jderobot");

    /**
     * Interface to the Gazebo Motors Actuators interaction.
     **/
    jderobot.Motors = Slice.defineObject(
        undefined,
        Ice.Object, undefined, 1,
        [
            "::Ice::Object",
            "::jderobot::Motors"
        ],
        -1, undefined, undefined, false);

    jderobot.MotorsPrx = Slice.defineProxy(Ice.ObjectPrx, jderobot.Motors.ice_staticId, undefined);

    Slice.defineOperations(jderobot.Motors, jderobot.MotorsPrx,
    {
        "getV": [, , , , , [5], , , , , ],
        "setV": [, , , , , [3], [[5]], , , , ],
        "getW": [, , , , , [5], , , , , ],
        "setW": [, , , , , [3], [[5]], , , , ],
        "getL": [, , , , , [5], , , , , ],
        "setL": [, , , , , [3], [[5]], , , , ]
    });

    jderobot.SetterMotors = Slice.defineObject(
        undefined,
        Ice.Object, undefined, 1,
        [
            "::Ice::Object",
            "::jderobot::SetterMotors"
        ],
        -1, undefined, undefined, false);

    jderobot.SetterMotorsPrx = Slice.defineProxy(Ice.ObjectPrx, jderobot.SetterMotors.ice_staticId, undefined);

    Slice.defineOperations(jderobot.SetterMotors, jderobot.SetterMotorsPrx,
    {
        "setMotors": [, , , , , , [["jderobot.MotorsPrx"]], , , , ]
    });
    exports.jderobot = jderobot;
}
(typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? module : undefined,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? require : this.Ice.__require,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? exports : this));
