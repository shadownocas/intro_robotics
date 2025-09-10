#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class RemoteController:
    def __init__(self):
        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

    def control(self, linear_vel, angular_vel):
        msg = Twist()
        msg.linear.x = linear_vel
        msg.angular.z = angular_vel #it rotates in z
        #just sending info,, diff de action em que o robo tbm tem de enviar info back
        self.cmd_pub.publish(msg) 

if __name__ == '__main__':
    rospy.init_node("robot_controller")
    controller = RemoteController()
    vel = -2 #-2m/s
    rate = rospy.Rate(10) #every 0.1 secs we send command,, 10Hz
    counter = 0
    try: 
        while not rospy.is_shutdown():
            if counter == 20:
                vel = -vel
                counter = 0
            
            controller.control(vel, 0)
            rate.sleep()
            counter += 1

    except rospy.ROSInterruptException:
        rospy.loginfo("Got interrupt message")
    
    rospy.loginfo("Closing remote")
