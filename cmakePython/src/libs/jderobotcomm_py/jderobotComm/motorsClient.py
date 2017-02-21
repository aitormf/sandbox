import Ice
import rospy
from .ice.motorsIceClient import MotorsIceClient
from .ros.publisherMotors import PublisherMotors

def __getMotorsIceClient(ic, prefix):
	'''
    Returns a Motors Ice Client. This function should never be used. Use getMotorsClient instead of this

    @param ic: Ice Communicator
    @param prefix: prefix name of client in config file

    @type ic: Ice Communicator
    @type prefix: String

    @return Motors Ice Client

    '''
	print("Publishing Motors with ICE interfaces")
	client = MotorsIceClient(ic, prefix)
	client.start()
	return client

def __getPublisherMotors(ic, prefix):
	'''
    Returns a Motors ROS Publisher. This function should never be used. Use getMotorsClient instead of this

    @param ic: Ice Communicator
    @param prefix: prefix name of client in config file

    @type ic: Ice Communicator
    @type prefix: String

    @return Motors ROS Publisher

    '''
	print("Publishing Motors with ROS messages")
	prop = prop = ic.getProperties()
	topic = prop.getPropertyWithDefault(prefix+".Topic","");
	client = PublisherMotors(topic)
	return client

def __Motorsdisabled(ic, prefix):
	'''
    Prints a warning that the client is disabled. This function should never be used. Use getMotorsClient instead of this

    @param ic: Ice Communicator
    @param prefix: prefix name of client in config file

	@type ic: Ice Communicator
    @type prefix: String

    @return None

    '''
	print(prefix + " Disabled")
	return None

def getMotorsClient (ic, prefix, node=None):
	'''
    Returns a Motors Client.

    @param ic: Ice Communicator
    @param prefix: prefix name of client in config file
    @param node: ROS node

    @type ic: Ice Communicator
    @type prefix: String
    @type node: ROS node

    @return None if Motors is disabled

    '''
	prop = prop = ic.getProperties()
	server = prop.getPropertyAsIntWithDefault(prefix+".Server",0)

	cons = [__Motorsdisabled, __getMotorsIceClient, __getPublisherMotors]

	return cons[server](ic, prefix)