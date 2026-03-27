async def square_path():
    import omni.usd
    from pxr import UsdPhysics
    import asyncio
    
    stage = omni.usd.get_context().get_stage()
    
    def set_wheels(left, right):
        for joint in ["front_left_wheel_joint", "rear_left_wheel_joint"]:
            prim = stage.GetPrimAtPath(f"/World/Robot/{joint}")
            drive = UsdPhysics.DriveAPI.Apply(prim, "angular")
            drive.CreateTargetVelocityAttr(left)
            drive.CreateDampingAttr(1e10)
            drive.CreateStiffnessAttr(0.0)
        for joint in ["front_right_wheel_joint", "rear_right_wheel_joint"]:
            prim = stage.GetPrimAtPath(f"/World/Robot/{joint}")
            drive = UsdPhysics.DriveAPI.Apply(prim, "angular")
            drive.CreateTargetVelocityAttr(right)
            drive.CreateDampingAttr(1e10)
            drive.CreateStiffnessAttr(0.0)

    for side in range(4):
        print(f"Side {side+1} - forward")
        set_wheels(100.0, 100.0)
        await asyncio.sleep(3.0)
        print(f"Side {side+1} - turning")
        set_wheels(-50.0, 50.0)
        await asyncio.sleep(2.0)

    set_wheels(0.0, 0.0)
    print("Square path complete!")

import asyncio
asyncio.ensure_future(square_path())
print("Started square path!")
