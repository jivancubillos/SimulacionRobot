from custom_service.srv import Service
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from tkinter import filedialog
import time


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Service, 'Service', self.player_callback)
        self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 10)

    def player_callback(self, request, response):
        msg=Twist()
        msg.linear.y=0.0
        msg.linear.z=0.0
        msg.angular.x=0.0
        msg.angular.y=0.0
        file=filedialog.askopenfile(mode="r", title="Seleccionar archivo", filetypes=(("Archivo separado por comas", "*.csv"),))
        data= file.readline().split(",")
        while data!=0 and len(data)!=1:
            print(data)
            print(data[0])
            print(data[1])
            msg.linear.x=float(data[0])
            msg.angular.z=float(data[1])
            self.publisher_.publish(msg)
            print(data)
            data=file.readline().split(",")
            time.sleep(0.1)
        file.close()
        respone=None
        return response
            


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
