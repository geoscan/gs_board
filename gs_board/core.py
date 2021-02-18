#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_interfaces.srv import Time,Info,Live
from gs_interfaces.msg import SimpleBatteryState
from rospy import ServiceProxy
from std_msgs.msg import Bool

class BoardManager():

    def __init__(self):
        rospy.wait_for_service("geoscan/alive")
        rospy.wait_for_service("geoscan/board/get_time")
        rospy.wait_for_service("geoscan/board/get_uptime")
        rospy.wait_for_service("geoscan/board/get_flight_time")
        rospy.wait_for_service("geoscan/board/get_info")

        self.__alive = ServiceProxy("geoscan/alive",Live)
        self.__time_service = ServiceProxy("geoscan/board/get_time",Time)
        self.__uptime_service = ServiceProxy("geoscan/board/get_uptime",Time)
        self.__flight_time_service = ServiceProxy("geoscan/board/get_flight_time",Time)
        self.__info_service = ServiceProxy("geoscan/board/get_info",Info)
    
    def runStatus(self):
        return self.__alive().status

    def boardNumber(self):
        if self.runStatus():
            return self.__info_service().num
        else:
            rospy.logwarn("Wait, connecting to flight controller")

    def time(self):
        if self.runStatus():
            return self.__time_service().time
        else:
            rospy.logwarn("Wait, connecting to flight controller")

    def uptime(self):
        if self.runStatus():
            return self.__uptime_service().time
        else:
            rospy.logwarn("Wait, connecting to flight controller")

    def flightTime(self):
        if self.runStatus():
            return self.__flight_time_service().time
        else:
            rospy.logwarn("Wait, connecting to flight controller")