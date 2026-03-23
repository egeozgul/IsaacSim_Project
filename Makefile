SHELL=/bin/bash
ISAAC_PATH=/home/egeozgul/Documents/IsaacSim/isaac-sim-standalone-5.0.0-linux-x86_64

run_sim:
	source /opt/ros/jazzy/setup.bash && $(ISAAC_PATH)/isaac-sim.sh

run_ros:
	source /opt/ros/jazzy/setup.bash && ros2 launch ros/static_tf.launch.py

rviz:
	source /opt/ros/jazzy/setup.bash && rviz2 -d ros/assessment.rviz

test:
	source /opt/ros/jazzy/setup.bash && python3 sim/test_topics.py
