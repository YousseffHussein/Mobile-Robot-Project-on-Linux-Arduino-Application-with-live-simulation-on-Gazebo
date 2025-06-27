import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import numpy as np
import serial
import time

SerialObj = serial.Serial('/dev/ttyACM0') 

 
SerialObj.baudrate = 115200  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
#SerialObj.parity   ='N'    # No parity
#SerialObj.stopbits = 1     # Number of Stop bits = 1
time.sleep(3)



class CmdVelSubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.linear_and_angular_callback,
          10)
        

    
    def linear_and_angular_callback(self, msg):
        theta = msg.angular.z
        x_dot = msg.linear.x
        y_dot = msg.linear.y
        theta_dot = theta * math.pi / 180
        wheel_r = 25
        L = 279.33
        alpha_1 = 32.5 * math.pi / 180
        alpha_2 = 147.5 * math.pi / 180
        alpha_3 = 212.5 * math.pi / 180
        alpha_4 = -32.5 * math.pi / 180
        beta_1 = 57.5 * math.pi / 180
        beta_2 = -57.5 * math.pi / 180
        beta_3 = -122.5 * math.pi / 180
        beta_4 = 122.5 * math.pi / 180
        gamma_1 = -45 * math.pi / 180
        gamma_2 = -135 * math.pi / 180
        gamma_3 = 135 * math.pi / 180
        gamma_4 = 45 * math.pi / 180
        phi_dot_1 = 0
        phi_dot_2 = 0
        phi_dot_3 = 0
        phi_dot_4 = 0


        theta_I_dot = [[x_dot],
               [y_dot],
               [theta_dot]]

        angles_mat = [[math.sin(alpha_1 + beta_1 + gamma_1), -1 * math.cos(alpha_1 + beta_1 + gamma_1), -1 * L * math.cos(beta_1 + gamma_1)],
              [math.sin(alpha_2 + beta_2 + gamma_2), -1 * math.cos(alpha_2 + beta_2 + gamma_2), -1 * L * math.cos(beta_2 + gamma_2)],
              [math.sin(alpha_3 + beta_3 + gamma_3), -1 * math.cos(alpha_3 + beta_3 + gamma_3), -1 * L * math.cos(beta_3 + gamma_3)],
              [math.sin(alpha_4 + beta_4 + gamma_4), -1 * math.cos(alpha_4 + beta_4 + gamma_4), -1 * L * math.cos(beta_4 + gamma_4)]]

        phi_dot = [[phi_dot_1],
           [phi_dot_2],
           [phi_dot_3],
           [phi_dot_4]]


        phi_dot = np.dot(angles_mat, theta_I_dot)


        phi_dot[0] = phi_dot[0] / (wheel_r * math.cos(gamma_1))
        phi_dot[1] = phi_dot[1] / (wheel_r * math.cos(gamma_2))
        phi_dot[2] = phi_dot[2] / (wheel_r * math.cos(gamma_3))
        phi_dot[3] = phi_dot[3] / (wheel_r * math.cos(gamma_4))

        


# Define a format string for the floats

        format_string = "{:.2f}"
# Convert the column vector into a single line string with formatted floats
        phi_dot_string = '\n'.join(map(format_string.format, phi_dot[:, 0]))
        li = list(phi_dot_string.split(" "))
        
# Display the column vector
        for item in li:
            self.get_logger().info(item)
            SerialObj.write(item.encode())
            time.sleep(0.1)
        
def main(args=None):
    rclpy.init(args=args)

    cmd_vel_subscriber = CmdVelSubscriber()

    rclpy.spin(cmd_vel_subscriber)


if __name__ == '__main__':
    main()