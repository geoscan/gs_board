#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_interfaces.srv import Live, SetParametersList, ParametersList
from gs_interfaces.msg import Parameter
from rospy import ServiceProxy
from std_srvs.srv import Empty

class BoardManager():

    def __init__(self, namespace = ""):
        if namespace != "":
            namespace += "/"

        self.__alive = ServiceProxy(f"{namespace}geoscan/alive", Live)
        self.__restart = ServiceProxy(f"{namespace}geoscan/board/restart", Empty)
        self.__get_parameters_service = ServiceProxy(f"{namespace}geoscan/board/get_parameters", ParametersList)
        self.__set_parameters_service = ServiceProxy(f"{namespace}geoscan/board/set_parameters", SetParametersList)
    
    def runStatus(self):
        return self.__alive().status

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