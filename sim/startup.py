async def domain_rand_loop():
    import omni.usd
    import omni.replicator.core as rep
    import omni.graph.core as og
    import omni.kit.app
    import asyncio
    import random

    stage = omni.usd.get_context().get_stage()
    app = omni.kit.app.get_app()

    camera_path = "/World/Robot/base_link/bumblebee_stereo_camera_frame/bumblebee_stereo_left_frame/bumblebee_stereo_left_camera"
    lidar_path = "/World/Robot/base_link/lidar_frame/Example_Rotary"
    rp_camera = rep.create.render_product(camera_path, (640, 480))
    rp_lidar = rep.create.render_product(lidar_path, (1, 1))
    og.Controller.set(
        og.Controller.attribute("/World/ROS2_Graph/ros2_camera_helper.inputs:renderProductPath"),
        rp_camera.path
    )
    og.Controller.set(
        og.Controller.attribute("/World/ROS2_Graph/ros2_rtx_lidar_helper.inputs:renderProductPath"),
        rp_lidar.path
    )
    print("Sensors ready!")

    frame = 0
    while True:
        await app.next_update_async()
        frame += 1
        if frame % 300 == 0:
            light = stage.GetPrimAtPath("/World/DomeLight")
            if light.IsValid():
                intensity = random.uniform(500.0, 3000.0)
                light.GetAttribute("inputs:intensity").Set(intensity)
                print(f"Light: {intensity:.0f}")
            lidar = stage.GetPrimAtPath("/World/Robot/base_link/lidar_frame/Example_Rotary")
            if lidar.IsValid():
                noise = random.uniform(0.01, 0.05)
                lidar.GetAttribute("omni:sensor:Core:azimuthErrorStd").Set(noise)
                lidar.GetAttribute("omni:sensor:Core:elevationErrorStd").Set(noise)
                print(f"LiDAR noise: {noise:.3f}")

import asyncio
if not hasattr(asyncio, '_domain_rand_running'):
    asyncio._domain_rand_running = True
    asyncio.ensure_future(domain_rand_loop())
    print("Domain rand started!")
else:
    print("Already running!")
