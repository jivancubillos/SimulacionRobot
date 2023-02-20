import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame, sys
from pygame.locals import *


pygame.init()
     
    # Colours
BACKGROUND = (255, 255, 255)
     
    # Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
     
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')
WINDOW.fill(BACKGROUND)
FULLBLUE=(0,0,255)

mx= WINDOW_WIDTH /5
my=-WINDOW_HEIGHT/5


def transformacion(point:tuple,mx:float,my:float)->tuple:
    xt=point[0]
    yt=point[0]
    xd=mx*(xt+2.5)
    yd=my*(yt-2.5)
    return (xd,yd)
    
    
   

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
        global mx
        global my
        p0=transformacion((self.x[len(self.x)-2], self.y[len(self.y)-2]),mx,my)
        p1=transformacion((self.x[len(self.x)-1], self.y[len(self.y)-1]),mx,my)
        pygame.draw.line(WINDOW, FULLBLUE,p0 ,p1 , 3)
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

