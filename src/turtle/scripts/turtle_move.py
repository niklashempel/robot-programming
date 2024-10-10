#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

rospy.init_node("moveIt")

pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
rate = rospy.Rate(2)

msg = Twist()
msg.angular.x = 0
msg.angular.y = 0
msg.angular.z = 1

msg.linear.x = 2.0
msg.linear.y = 0
msg.linear.z = 0

while not rospy.is_shutdown():
    pub.publish(msg)
    rate.sleep()