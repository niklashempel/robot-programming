#!/usr/bin/python3

import rospy
from custom_msg.msg import Test
import random
rospy.init_node("nodey")
rate = rospy.Rate(1)
pub = rospy.Publisher("service1", Test, queue_size=10)

rospy.loginfo("Initialized")
t = Test()

while not rospy.is_shutdown():
    t.x = random.randrange(100, 500)
    t.y = random.randrange(100, 500)
    pub.publish(t)
    rate.sleep()