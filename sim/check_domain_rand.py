import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image
import numpy as np

class DomainRandChecker(Node):
    def __init__(self):
        super().__init__('domain_rand_checker')
        
        self.lidar_msgs = []
        self.camera_msgs = []
        
        self.create_subscription(PointCloud2, '/point_cloud',
            self.lidar_cb, 10)
        self.create_subscription(Image, '/camera',
            self.camera_cb, 10)
            
        self.timer = self.create_timer(10.0, self.check)
        self.get_logger().info('Checking domain randomization for 10 seconds...')

    def lidar_cb(self, msg):
        self.lidar_msgs.append(msg)

    def camera_cb(self, msg):
        # Store mean brightness of image
        data = np.frombuffer(msg.data, dtype=np.uint8)
        self.camera_msgs.append(float(np.mean(data)))

    def check(self):
        print("\n===== DOMAIN RANDOMIZATION CHECK =====")
        
        if len(self.camera_msgs) > 1:
            brightness_std = np.std(self.camera_msgs)
            print(f"Camera brightness std: {brightness_std:.2f}")
            if brightness_std > 5.0:
                print("✅ Camera brightness is varying (light randomization working)")
            else:
                print("❌ Camera brightness not varying enough")
        
        print(f"LiDAR messages received: {len(self.lidar_msgs)}")
        print(f"Camera messages received: {len(self.camera_msgs)}")
        print("=======================================")
        rclpy.shutdown()

def main():
    rclpy.init()
    node = DomainRandChecker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
