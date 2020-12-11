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
* __time_service - rospy.ServiceProxy: gs_interfaces.srv.Time
* __uptime_service - rospy.ServiceProxy: gs_interfaces.srv.Time
* __flight_time_service - rospy.ServiceProxy: gs_interfaces.srv.Time
* __info_service - rospy.ServiceProxy: gs_interfaces.srv.Info

#### Методы:
* runStatus - возвращает статус подключения RPi к Pioneer
* boardNumber - возвращает имя/номер платы
* time - возвращает время с момента включения коптера
* uptime - возвращает время запуска для системы навигации
* flightTime - возвращает время с начала полета

#### Используемые сервисы:
* geoscan/board/get_info (gs_interfaces/Info)
* geoscan/board/get_time (gs_interfaces/Time)
* geoscan/board/get_uptime (gs_interfaces/Time)
* geoscan/board/get_flight_time (gs_interfaces/Time)

## Необходимые пакеты:
ROS:
* gs_interfaces
* gs_core

## Примечание:
Все классы в данном пакете могут быть использованы только при запущеной ноде ros_plaz_node.py из пакета gs_core