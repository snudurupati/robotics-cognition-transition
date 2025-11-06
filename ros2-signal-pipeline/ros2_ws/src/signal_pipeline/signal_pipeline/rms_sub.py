import collections, math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class RmsSubscriber(Node):
    def __init__(self):
        super().__init__('rms_sub')
        self.declare_parameter('window',60)
        self.window=collections.deque(maxlen=int(self.get_parameter('window').value))
        self.sub=self.create_subscription(Float32,'signal',self.cb,10)
    def cb(self,msg:Float32):
        self.window.append(float(msg.data))
        if len(self.window)==self.window.maxlen:
            rms=math.sqrt(sum(x*x for x in self.window)/len(self.window))
            self.get_logger().info(f'RMS({len(self.window)}): {rms:.4f}')
def main():
    rclpy.init(); node=RmsSubscriber(); rclpy.spin(node); node.destroy_node(); rclpy.shutdown()
