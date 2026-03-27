SHELL=/bin/bash
ISAAC_PATH=/home/egeozgul/Documents/IsaacSim/isaac-sim-standalone-5.0.0-linux-x86_64
ASSESSMENT_PATH=/home/egeozgul/isaac_ros_assessment

run_sim:
	source /opt/ros/jazzy/setup.bash && $(ISAAC_PATH)/isaac-sim.sh

rviz:
	source /opt/ros/jazzy/setup.bash && rviz2 -d $(ASSESSMENT_PATH)/ros/assessment.rviz

run_ros:
	source /opt/ros/jazzy/setup.bash && ros2 launch $(ASSESSMENT_PATH)/ros/static_tf.launch.py

test:
	source /opt/ros/jazzy/setup.bash && python3 $(ASSESSMENT_PATH)/sim/test_topics.py

check_topics:
	source /opt/ros/jazzy/setup.bash && ros2 topic list

hz_lidar:
	source /opt/ros/jazzy/setup.bash && ros2 topic hz /point_cloud

hz_camera:
	source /opt/ros/jazzy/setup.bash && ros2 topic hz /camera

bag_record:
	source /opt/ros/jazzy/setup.bash && ros2 bag record -o $(ASSESSMENT_PATH)/bags/demo_bag /point_cloud /camera /odom /tf /clock

help:
	@echo "Available commands:"
	@echo "  make run_sim      - Launch Isaac Sim"
	@echo "  make rviz         - Launch RViz with assessment config"
	@echo "  make run_ros      - Launch ROS2 static TF publishers"
	@echo "  make test         - Run topic smoke tests"
	@echo "  make check_topics - List all active ROS2 topics"
	@echo "  make hz_lidar     - Check LiDAR publish rate"
	@echo "  make hz_camera    - Check camera publish rate"
	@echo "  make bag_record   - Record a rosbag"

.PHONY: run_sim rviz run_ros test check_topics hz_lidar hz_camera bag_record help
