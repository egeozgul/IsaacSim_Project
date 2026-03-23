run_sim:
	cd ~/Documents/IsaacSim/isaac-sim-standalone-5.0.0-linux-x86_64/ && ./isaac-sim.sh

run_ros:
	ros2 launch ros/static_tf.launch.py

rviz:
	rviz2 -d ros/assessment.rviz

test:
	python3 sim/test_topics.py
