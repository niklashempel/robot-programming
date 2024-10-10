#!/usr/bin/python3

import rospy
from std_msgs.msg import String

rospy.init_node("noname")
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    my_msg = rospy.get_param("~Hello", "???") # Parameter defined in launch file
    rospy.loginfo(my_msg)
    rate.sleep()