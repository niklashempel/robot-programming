#!/usr/bin/python3
import rospy
from std_msgs import msg
def callback(data):
  rospy.loginfo("[" + rospy.get_caller_id() +"] " + "Received: %s", data.data)

def listener():
  rospy.init_node('node2', anonymous=True)
  rospy.Subscriber("topic12", msg.String, callback)
  rospy.spin()

if __name__ == '__main__':
  listener()
