Run package via

```sh
roslaunch parameters param.launch
```

The launch file sets the private parameter "Hello" for each node. The parameter can also be set via command line.

```sh
rosparam set /Alice/Hello 123
```
