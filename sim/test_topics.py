import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, Image
from nav_msgs.msg import Odometry
from tf2_msgs.msg import TFMessage
from rosgraph_msgs.msg import Clock
import sys

class TopicTester(Node):
    def __init__(self):
        super().__init__('topic_tester')
        self.required_topics = {
            '/point_cloud': 3.0,
            '/camera': 10.0,
            '/tf': 30.0,
            '/odom': 3.0,
            '/clock': 30.0
        }
        self.counts = {t: 0 for t in self.required_topics}
        self.create_subscription(PointCloud2, '/point_cloud', lambda m: self.cb('/point_cloud'), 10)
        self.create_subscription(Image, '/camera', lambda m: self.cb('/camera'), 10)
        self.create_subscription(Odometry, '/odom', lambda m: self.cb('/odom'), 10)
        self.create_subscription(TFMessage, '/tf', lambda m: self.cb('/tf'), 10)
        self.create_subscription(Clock, '/clock', lambda m: self.cb('/clock'), 10)
        self.create_timer(5.0, self.check_results)
        self.get_logger().info('Testing topics for 5 seconds...')

    def cb(self, topic):
        self.counts[topic] += 1

    def check_results(self):
        print("\n===== SMOKE TEST RESULTS =====")
        all_passed = True
        for topic, min_hz in self.required_topics.items():
            actual_hz = self.counts[topic] / 5.0
            passed = actual_hz >= min_hz
            status = "✅ PASS" if passed else "❌ FAIL"
            print(f"{status} {topic}: {actual_hz:.1f} Hz (min: {min_hz} Hz)")
            if not passed:
                all_passed = False
        print("==============================")
        print("OVERALL:", "✅ ALL PASSED" if all_passed else "❌ SOME FAILED")
        rclpy.shutdown()
        sys.exit(0 if all_passed else 1)

def main():
    rclpy.init()
    node = TopicTester()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
