import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('__TEMPLATE_NODE_NAME')

        self.declare_parameter('int_number', 5)


        self.publisher_ = self.create_publisher(Int16, 'a', 10)
        self.subscriber = self.create_subscription(Int16, 'b', self.callback, 10)

    def callback(self, msg):
        pass


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()