#!/usr/bin/env python
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# **********************************************************************

import sys, traceback, Ice

Ice.loadSlice('Callback.ice')
import Demo

proxyClient = None

class CallbackI(Demo.Callback):
    def initiateCallback(self, proxy, current=None):
        print("initiating callback to: " + current.adapter.getCommunicator().proxyToString(proxy))
        global proxyClient
        proxyClient = proxy

    def shutdown(self, current=None):
        print("shutting down...")
        current.adapter.getCommunicator().shutdown()


endpoint = "tcp -h localhost -p 10000"
id = Ice.InitializationData()
ic = Ice.initialize(sys.argv, id)
adapter = ic.createObjectAdapterWithEndpoints("callback",endpoint)
adapter.add(CallbackI(), ic.stringToIdentity("callback"))
adapter.activate()
i = 0
while True:
            if proxyClient:
                proxyClient.callback(i)
                i=i+1

