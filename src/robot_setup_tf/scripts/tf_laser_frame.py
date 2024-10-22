#!/usr/bin/python3

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node("fixed_tf_broadcaster")
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        br.sendTransform((0.0, 2.0, 0.0), # 2 meters above the origin
                         (0.0, 0.0, 0.0, 1.0), # No rotation because (x,y,z,w) = (0,0,0,1) and w = cos(theta/2) and arccos(1) = 0
                         rospy.Time.now(),
                         "laser", # Name of the new frame
                         "turtle1") # Name of the parent
        rate.sleep()