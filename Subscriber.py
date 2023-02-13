

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from matplotlib import pyplot as plt


   

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'turtlebot_position',
            self.listener_callback,
            10)
        self.x=[]
        self.y=[]
        self.subscription  # prevent unused variable warning


    def listener_callback(self, msg):
        self.x.append(msg.linear.x)
        self.y.append(msg.linear.y)
        print(msg.linear.x)
        print(self.x)
        plt.figure(1)
        plt.plot(self.x,self.y)
        
        
        
        
        
        

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()
    
  
    

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    












# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Twist
# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
# import threading

# x=[]
# y=[]
# fig, ax = plt.subplots()

# def animate(i):
#     global x
#     global y
#     ax.clear()
#     ax.plot(x,y)
#     print(x)
# def animation():
#     ani=FuncAnimation(fig, animate, interval=200)
#     plt.show()
    

# class MinimalSubscriber(Node):

#     def __init__(self):
#         super().__init__('minimal_subscriber')
#         self.subscription = self.create_subscription(
#             Twist,
#             'turtlebot_position',
#             self.listener_callback,
#             10)
#         self.subscription  # prevent unused variable warning


#     def listener_callback(self, msg):
#         global x
#         global y
#         x.append(msg.linear.x)
#         y.append(msg.linear.y)
#         print(msg.linear.x)
        
        
        

# def main(args=None):
#     rclpy.init(args=args)

#     minimal_subscriber = MinimalSubscriber()
    
#     plotter= threading.Thread(target=animation())
#     plotter.start()
    

#     rclpy.spin(minimal_subscriber)

#     # Destroy the node explicitly
#     # (optional - otherwise it will be done automatically
#     # when the garbage collector destroys the node object)
#     minimal_subscriber.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()
    
    
    
    
    
    
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from matplotlib import pyplot as plt


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'turtlebot_position',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.x=[]
        self.y=[]
        self.fig, self.ax = plt.subplots()
        plt.show()

    def listener_callback(self, msg):
        self.x.append(msg.data.linear.x)
        self.y.append(msg.data.linear.y)
        print(self.x,self.y)
        
        self.ax.clear()
        self.ax.plot(self.x,self.y)
        
        
   
        
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()"""