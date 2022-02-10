#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_interfaces.srv import Time, Info, Live, SetParametersList, ParametersList
from gs_interfaces.msg import SimpleBatteryState, Parameter
from rospy import ServiceProxy
from std_msgs.msg import Bool
from std_srvs.srv import Empty

class BoardManager():
    def __init__(self):
        rospy.wait_for_service("geoscan/alive")
        rospy.wait_for_service("geoscan/board/restart")
        rospy.wait_for_service("geoscan/board/get_time")
        rospy.wait_for_service("geoscan/board/get_uptime")
        rospy.wait_for_service("geoscan/board/get_flight_time")
        rospy.wait_for_service("geoscan/board/get_info")
        rospy.wait_for_service("geoscan/board/get_parameters")
        rospy.wait_for_service("geoscan/board/set_parameters")

        self.__alive = ServiceProxy("geoscan/alive",Live)
        self.__restart = ServiceProxy("geoscan/board/restart", Empty)
        self.__time_service = ServiceProxy("geoscan/board/get_time", Time)
        self.__uptime_service = ServiceProxy("geoscan/board/get_uptime", Time)
        self.__flight_time_service = ServiceProxy("geoscan/board/get_flight_time", Time)
        self.__info_service = ServiceProxy("geoscan/board/get_info", Info)
        self.__get_parameters_service = ServiceProxy("geoscan/board/get_parameters", ParametersList)
        self.__set_parameters_service = ServiceProxy("geoscan/board/set_parameters", SetParametersList)
    
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

    def restart(self):
        self.__restart()

    def getParameters(self):
        params = self.__get_parameters_service().params
        params_dict = {}
        for param in params:
            params_dict.update({param.name: param.value})

        return params_dict

    def setParameters(self, params_dict):
        params = []
        for name in params_dict:
            params.append(Parameter(name, params_dict[name]))

        return self.__set_parameters_service(params).status