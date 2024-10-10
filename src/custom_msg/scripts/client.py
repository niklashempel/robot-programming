#!/usr/bin/python3
import rospy
from custom_msg.msg import Test
from custom_msg.srv import add

def add_two_ints_client(x, y):
    rospy.loginfo("params = %f, %f" % (x,y))
    rospy.wait_for_service("add_x_y")
    add_two_ints = rospy.ServiceProxy("add_x_y", add)
    res = add_two_ints(x,y)
    return res.sum

def callback(data):
    response = add_two_ints_client(data.x, data.y)
    rospy.loginfo("response: %f" % response)

if __name__ == "__main__":
    rospy.init_node("nodex", anonymous=False)
    response = add_two_ints_client(10,10)
    rospy.loginfo("response = %f", response)
    sub = rospy.Subscriber("service1", Test, callback)
    rospy.spin()