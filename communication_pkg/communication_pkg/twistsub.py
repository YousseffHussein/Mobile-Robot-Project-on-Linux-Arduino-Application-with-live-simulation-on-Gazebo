import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelSubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.linear_and_angular_callback,
            10)

    def linear_and_angular_callback(self, msg):
        self.get_logger().info('x: [%f] y: [%f] Angular velocity: [%f]' % (
            msg.linear.x, msg.linear.y, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)

    cmd_vel_subscriber = CmdVelSubscriber()

    rclpy.spin(cmd_vel_subscriber)

    cmd_vel_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()