#!/usr/bin/python3
import rospy
from std_msgs.msg import String, Float32

def callback(data):
  rospy.loginfo("[" + rospy.get_caller_id() +"] " + "Received: %s", data.data)

if __name__ == '__main__':
  rospy.init_node('node1')
  rospy.Subscriber("topic31", Float32, callback)
  rospy.init_node('node1')
  pub = rospy.Publisher('topic12', String, queue_size=10)
  rate = rospy.Rate(1)
  try:
    while not rospy.is_shutdown():
      pub.publish("hello world")
      rospy.loginfo("[" + rospy.get_caller_id() + "] hello world sent")
      rate.sleep()
  except rospy.ROSInterruptException:
    pass 

# count = 0
# def callback(data):
#   global count
#   count = data.data