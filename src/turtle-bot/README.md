## Installing TurtleBot3 Packages

```sh
sudo apt-get update
sudo apt install ros-noetic-turtlebot3
sudo apt install ros-noetic-turtlebot3-simulations
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
```

## Launch Simulation

```sh
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```
