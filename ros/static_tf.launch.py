from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0.3', '0', '0', '0', 'base_link', 'lidar_frame']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.25', '0', '0.2', '0', '0', '0', 'base_link', 'camera_frame']
        ),
    ])
