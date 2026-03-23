from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import omni.usd
import omni

# Load the scene
omni.usd.get_context().open_stage("/home/egeozgul/isaac_ros_assessment/assets/custom_scene.usd")

# Keep running
while simulation_app.is_running():
    simulation_app.update()

simulation_app.close()
