import rclpy
from rclpy.node import Node
from pynput import keyboard as kb
from geometry_msgs.msg import Twist
import threading

Key= None

def pulsa(tecla):
    global Key
    Key=tecla
    print("la tecla es", Key)
def suelta(tecla):
    global Key
    Key="p"
    
def listener():
    k=kb.Listener(pulsa,suelta)
    k.run()


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('turtlebot_teleop')
        self.publisher_ = self.create_publisher(Twist, '/turtlebot_cmdVel', 10)
        self.velx=float(input("ingrese la velocidad lineal: "))
        self.velz=float(input("ingrese la velocidad angular: "))
        timer_period = 0.1 # seconds
        self.timer = self.create_timer(timer_period, self.callback)
        
        
        
    def callback(self):
        msg = Twist()
        global Key
        if Key== kb.KeyCode.from_char('w'):
            msg.linear.x = self.velx
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x= 0.0
            msg.angular.y= 0.0
            msg.angular.z= 0.0
        elif Key== kb.KeyCode.from_char('s'):
             msg.linear.x = -self.velx
             msg.linear.y = 0.0
             msg.linear.z = 0.0
             msg.angular.x= 0.0
             msg.angular.y= 0.0
             msg.angular.z= 0.0
        elif Key== kb.KeyCode.from_char('a'):
             msg.linear.x = 0.0
             msg.linear.y = 0.0
             msg.linear.z = 0.0
             msg.angular.x= 0.0
             msg.angular.y= 0.0
             msg.angular.z= self.velz
        elif Key== kb.KeyCode.from_char('d'):
            msg.linear.x = 0.0
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x= 0.0
            msg.angular.y= 0.0
            msg.angular.z= -self.velz
        elif Key== "p":
            msg.linear.x = 0.0
            msg.linear.y = 0.0
            msg.linear.z = 0.0
            msg.angular.x= 0.0
            msg.angular.y= 0.0
            msg.angular.z= 0.0
        self.publisher_.publish(msg)
        print(Key)
       
    
        


def main(args=None):
    
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()
    
    hilo=threading.Thread(target=listener)
    hilo.start()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()