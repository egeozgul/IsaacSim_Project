# Architecture Diagram

## Data Flow
```
┌────────────────────────────────────────────────────┐
│                    Isaac Sim 5.0.0                          │
│                                                             │
│  ┌─────────────┐    ┌──────────────┐                   │
│  │ Custom USD     │    │ Action Graph   │                   │
│  │   Scene        │──▶│  ROS2_Graph    │                   │
│  │                │    │                │                   │
│  │ • Robot        │    │ • Clock pub    │                   │
│  │ • LiDAR        │    │ • LiDAR pub    │                   │
│  │ • Camera       │    │ • Camera pub   │                   │
│  │ • Objects      │    │ • Odom pub     │                   │
│  │ • Lights       │    │ • TF pub       │                   │
│  └─────────────┘    └──────┬───────┘                   │
│                                │                            │
│              ROS2 Bridge       │                            │
│         (isaacsim.ros2.bridge)                              │
└────────────────────────────┼──────────────────────┘
                                   │
                          ROS2 Jazzy Topics
                                  │
          ┌───────────────────┼───────────────────┐
          │                       │                      │
     /point_cloud             /camera                   /tf
     /clock                    /odom                 /tf_static
          │                       │                      │
          └───────────────────┼───────────────────┘
                                  │
                                RViz2
                                  │
                    ┌─────────────────┐
                    │ • PointCloud2.     │
                    │ • Image            │
                    │ • TF frames        │
                    │ • Odometry         │
                    └─────────────────┘
```

## TF Tree
```
World
└── base_link (robot body, moves with physics)
    ├── front_left_wheel_link
    ├── front_right_wheel_link
    ├── rear_left_wheel_link
    ├── rear_right_wheel_link
    ├── lidar_frame (RTX LiDAR mount)
    └── camera_frame (Bumblebee camera mount)
```

## Domain Randomization
```
Every 300 frames (~5 seconds):
┌─────────────────────────────────┐
│  DomeLight intensity                  │
│  500 ──────────────────▶ 3000     │
│                                       │
│  LiDAR azimuth noise std              │
│  0.01 ─────────────────▶ 0.05      │
│                                       │
│  LiDAR elevation noise std            │
│  0.01 ─────────────────▶ 0.05      │
└─────────────────────────────────┘
```
