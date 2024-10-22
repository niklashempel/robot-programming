#!/usr/bin/python3

import rospy
import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta), # https://en.wikipedia.org/wiki/Euler_angles
                     rospy.Time.now(),
                     turtlename,
                     "world")
    
if __name__ == '__main__':
    rospy.init_node("robot_tf_pub", anonymous=False)
    turtle_name = rospy.get_param("~turtle", "turtle1")
    rospy.Subscriber("%s/pose" % turtle_name, turtlesim.msg.Pose, handle_turtle_pose, turtle_name) # Broadcast a message every time a new message is received
    rospy.spin()