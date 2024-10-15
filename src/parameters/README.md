Run package via

```sh
roslaunch parameters param.launch
```

The launch file sets the private parameter "Hello" for each node. The parameter can also be set via command line.

```sh
rosparam set /Alice/Hello 123
```

## Parameters

Setting the Global parameter "/robot_name" to the value "TurtleBot3"

```py
rospy.set_param('/robot_name', 'TurtleBot3') # Public parameter
```

Private parameters are used when you need setting specific to one node, sch as internal configurations or senstive data that should not be accessible system-wide.

```py
rospy.set_param('~robot_speed', 1.5) # Private parameter
```

To get the name:

```py
rospy.get_param('~robot_speed', 10.0) # Default to 10 if param is not set
```

Other functions to manage parameters in ROS:

- rospy.has_param(param_name)
- rospy.delete_param(param_name)
- rospy.search_param(param_name)
- rospy.get_param_names()
