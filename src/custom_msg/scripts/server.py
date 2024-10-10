#!/usr/bin/python3
import rospy
from custom_msg.srv import add, addResponse

def handle_add_two_ints(req):
    rospy.loginfo("Returning [%s + %s = %s]"%(req.a, req.b, (req.a+req.b)))
    return addResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node("add_two_ints_server") 
    rospy.Service("add_x_y", add, handle_add_two_ints) # name is important since we use it in the client
    rospy.loginfo("Ready to add two float32.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()