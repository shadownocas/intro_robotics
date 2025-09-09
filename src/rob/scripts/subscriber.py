#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class FastSubscriber:
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, Float32, self.fastCallback)
    def fastCallback(self, ros_data):
        rospy.loginfo("FastCallback: " + str(ros_data.data)) #rosmsg show <nome_msg> com este comando conseguimos saber os parametros


class SlowSubscriber:
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, Float32, self.slowCallback)
    def slowCallback(self, ros_data):
        rate = rospy.Rate(1)
        for i in range(0, 5):
            rate.sleep()

        rospy.loginfo("slowCallback: " + str(ros_data.data))



if __name__ == "__main__":
    rospy.init_node("double_subscriber")

    subscriber_fast = FastSubscriber("topic_1")
    subscriber_slow = SlowSubscriber("topic_2")

    rospy.spin() #keeps executinguntil we ctrl + C
