# ros2-signal-pipeline
Minimal ROS2 pipeline for Week 4: sine publisher + RMS subscriber (rclpy), params, launch, rosbag.

## Build/Run
```
source /opt/ros/<distro>/setup.bash
cd ros2_ws
colcon build
source install/setup.bash
ros2 launch signal_pipeline pipeline.launch.py
```
## Record/Analyze
```
ros2 bag record /signal -o bags/signal_bag
# after ~60s Ctrl+C
ros2 bag info bags/signal_bag
python3 src/signal_pipeline/signal_pipeline/analyze_bag.py bags/signal_bag
```
