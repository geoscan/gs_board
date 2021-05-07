# Описание пакета gs_board

# Описание:
В данном пакете представлены инструменты для получение бортовой информации

## Состав пакета:
Классы:
* BoardManager

## Описание классов:

### 1. BoardManager
Класс менеджера бортовой информации

#### Инициализация:
Без параметров

#### Поля:
* __alive - rospy.ServiceProxy: gs_interfaces.srv.Live
* __restart - rospy.ServiceProxy: std_srvs.srv.Empty
* __time_service - rospy.ServiceProxy: gs_interfaces.srv.Time
* __uptime_service - rospy.ServiceProxy: gs_interfaces.srv.Time
* __flight_time_service - rospy.ServiceProxy: gs_interfaces.srv.Time
* __info_service - rospy.ServiceProxy: gs_interfaces.srv.Info
* __get_parameters_service - rospy.ServiceProxy: gs_interfaces.srv.ParametersList
* __set_parameters_service - rospy.ServiceProxy: gs_interfaces.srv.SetParametersList

#### Методы:
* runStatus - возвращает статус подключения RPi к базовой плате Пионер
* boardNumber - возвращает имя/номер платы
* time - возвращает время с момента включения коптера
* uptime - возвращает время запуска для системы навигации
* flightTime - возвращает время с начала полета
* restart - перезапуск базовой платы Пионер
* getParameters - возвращает параметры АП
* setParameters(params_dict) - устанавливает параметры АП, params_dict - словарь параметров (название_параметра:значение_параметра)

#### Используемые сервисы:
* geoscan/alive (gs_interfaces/Live)
* geoscan/board/restart (std_srvs/Empty)
* geoscan/board/get_info (gs_interfaces/Info)
* geoscan/board/get_time (gs_interfaces/Time)
* geoscan/board/get_uptime (gs_interfaces/Time)
* geoscan/board/get_flight_time (gs_interfaces/Time)
* geoscan/board/get_parameters (gs_interfaces/ParametersList)
* geoscan/board/set_parameters (gs_interfaces/SetParametersList) 

## Необходимые пакеты:
ROS:
* gs_interfaces
* gs_core
* std_srvs

## Примечание:
Все классы в данном пакете могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core