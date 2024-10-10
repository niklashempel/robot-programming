#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32

def publisher():
    rospy.init_node('node3')
    rate = rospy.Rate(0.5)
    pub = rospy.Publisher('topic31', Float32, queue_size=10)
    count = 0
    while not rospy.is_shutdown():
        rospy.loginfo("[" + rospy.get_caller_id() +"] " + "Sent %0.1f", count)
        pub.publish(count)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass 
