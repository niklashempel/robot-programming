#!/usr/bin/python3

import rospy
from turtlesim.srv import TeleportAbsolute # Type of service

def reset_turtle_position():
    # Wait for teleport service to be available
    rospy.wait_for_service("/turtle1/teleport_absolute") # Blocking

    try:
        # Create a handle for the service
        teleport = rospy.ServiceProxy("/turtle1/teleport_absolute", TeleportAbsolute)

        # Reset the turtle's position (x=5.5, y=5.5, theta=0)
        x = rospy.get_param("/startX")
        y = rospy.get_param("/startY")

        teleport(x, y, 0)
        rospy.loginfo("Turtle position reset to (" + str(x) + ", " + str(y) + ") with heading 0.")

    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == "__main__":
    rospy.init_node("reset_turtle_position_node")
    reset_turtle_position()
