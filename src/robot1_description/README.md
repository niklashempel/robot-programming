# RVIZ

To start RVIZ with the robot model, run the following command:

```bash
roslaunch robot1_description view_robot.launch
```

To create a new RVIZ configuration, do the following steps:

1. mkdir urdf launch config
2. touch urdf/robot1.urdf
3. touch launch/view_robot.launch
4. touch config/view_robot.rviz
5. Run ```bash rosrun rviz rviz``` and save default configuration to config/view_robot.rviz
6. Fill in the urdf/robot1.urdf file with the robot description
7. Run ```bash roslaunch robot1_description view_robot.launch```
8. Load model via Add > RobotModel

![Add Robot Model](<Screenshot.png>)