# TF

[tf](http://wiki.ros.org/tf) is a package that lets the user keep track of multiple coordinate frames over time. It maintains the relationship between coordinate frames in a tree structure buffered in time, and lets the user transform points, vectors, etc between any two coordinate frames at any desired point in time.

This package contains two nodes `turtle1` and `turtle2` where the latter one follows the former one (with some delay). The `turtle1` node also contains a laser frame on top of it.

To run the nodes, execute the following command:

```bash
roslaunch robot_setup_tf start_demo.launch
```