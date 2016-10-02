#!/usr/bin/env python
# coding=utf-8

import rospy
import time  			#librería para las pausas.
from std_msgs.msg import Int32	#librería para los mensajes enviados.

giro=0			#guarda el sentido del giro que realiza.
encoder_inicio = 0  	#valor para la lectura del encoder.
vel=1
def listener():


    rospy.init_node('listener', anonymous=True)					#Se inicializa el nodo.
    pub1 = rospy.Publisher('ArduinoMotor/speed1', Int32, queue_size=10)
    pub2 = rospy.Publisher('ArduinoMotor/speed2', Int32, queue_size=10)
    time.sleep(1)  # Pausa en segundos.

    pub1.publish(vel)
    pub2.publish(giro)
    rospy.spin()


if __name__ == '__main__':
    listener()

