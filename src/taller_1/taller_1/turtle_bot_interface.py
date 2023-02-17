import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame, sys
from pygame.locals import *
import threading


pygame.init()
     
    # Colours
BACKGROUND = (255, 255, 255)
     
    # Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
     
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
WINDOW.fill(BACKGROUND)
FULLBLUE=(0,0,255)

   

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
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        
        pygame.draw.line(WINDOW, FULLBLUE, (self.x[len(self.x)-2], self.y[len(self.y)-2]), (self.x[len(self.x)-1], self.y[len(self.y)-1]), 3)
        rectangle1 = pygame.Rect(10, 30, 50, 70)
        pygame.draw.rect(WINDOW, FULLBLUE, rectangle1)
        pygame.display.update()
        fpsClock.tick(FPS)    
         
        
        
 
      
        
        

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


