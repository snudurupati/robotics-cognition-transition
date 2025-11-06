import math, time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class SignalPublisher(Node):
    def __init__(self):
        super().__init__('signal_pub')
        self.declare_parameter('frequency', 1.0)
        self.declare_parameter('amplitude', 1.0)
        self.pub=self.create_publisher(Float32,'signal',10)
        self.timer=self.create_timer(1.0/30.0,self.tick)
        self.t0=time.time()
    def tick(self):
        f=float(self.get_parameter('frequency').value)
        a=float(self.get_parameter('amplitude').value)
        t=time.time()-self.t0
        y=a*math.sin(2*math.pi*f*t)
        self.pub.publish(Float32(data=float(y)))
def main():
    rclpy.init(); node=SignalPublisher(); rclpy.spin(node); node.destroy_node(); rclpy.shutdown()
