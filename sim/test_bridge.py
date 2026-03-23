import sys
sys.path.insert(0, "/home/egeozgul/Documents/IsaacSim/isaac-sim-standalone-5.0.0-linux-x86_64/exts/isaacsim.ros2.bridge/jazzy/rclpy")

from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})

import omni
from omni.isaac.core import World

world = World()
world.scene.add_default_ground_plane()

# Enable ROS2 bridge
import omni.kit.app
manager = omni.kit.app.get_app().get_extension_manager()
manager.set_extension_enabled_immediate("isaacsim.ros2.bridge", True)

from omni.isaac.core.utils.extensions import enable_extension
enable_extension("isaacsim.ros2.bridge")

import rclpy
rclpy.init()

world.reset()
while simulation_app.is_running():
    world.step(render=True)

simulation_app.close()
