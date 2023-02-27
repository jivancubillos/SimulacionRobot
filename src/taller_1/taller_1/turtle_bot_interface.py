import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
from pygame.locals import *
import os
import pygame
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
from tkinter.filedialog import asksaveasfile
from custom_service.srv import Service
import threading

import numpy as np


import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


BACKGROUND = (255, 255, 255)
     
    # Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
     
root = tk.Tk()
embed = tk.Frame(root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT) #creates embed frame for pygame window
embed.grid(columnspan = (600), rowspan = 500) # Adds grid
embed.pack(side = LEFT) #packs window to the left
buttonwin = tk.Frame(root, width = 75, height = 500)
buttonwin.pack(side = LEFT)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
root.title('Interfaz')

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Recorrido en vivo')
WINDOW.fill(BACKGROUND)

FULLBLUE=(0,0,255)

mx= WINDOW_WIDTH /5
my=-WINDOW_HEIGHT/5

x=[]
y=[]
fig = plt.figure(1)
plt.ion()
plt.plot(x,y)




canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

def graph():
	global x
	global y
	plt.plot(x,y)
	plt.show()
	

button1 = Button(root, text = 'Guardar', command = lambda : graph())
button1.pack(side = TOP, pady = 0)


def abrirarchivo():
	archivo = filedialog.askopenfile(mode="r", title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"),))
	if archivo is not None:
		contenido = archivo.read()
		archivo.close()
		print(contenido)
        




pygame.init()
pygame.display.update()
root.update()






def transformacion(point:tuple,mx:float,my:float)->tuple:
    xt=point[0]
    yt=point[1]
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
        self.cli = self.create_client(Service, 'Service')
        self.req = Service.Request()
        button2=Button(root, text="Recorrido automático", command=self.send_request)
        button2.pack(side = TOP, pady = 100)
        root.update()
        
        self.subscription  # prevent unused variable warning
        

    def listener_callback(self, msg):
    	global x
    	global y
    	global mx
    	global my
    	x.append(msg.linear.x)
    	y.append(msg.linear.y)
    	p0=transformacion((x[len(x)-2], y[len(y)-2]),mx,my)
    	p1=transformacion((x[len(x)-1], y[len(y)-1]),mx,my)
    	pygame.draw.line(WINDOW, FULLBLUE,p0 ,p1 , 3)
    	pygame.display.update()
    	root.update()
    	fpsClock.tick(FPS)
    	

    	for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        
    
    def send_request(self):
        self.future = self.cli.call_async(self.req)
        #rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
        
    

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    
    hilo=threading.Thread(target=rclpy.spin(minimal_subscriber))
    hilo.start()
   
    
    
    

    minimal_subscriber.destroy_node()
    rclpy.shutdown()
    
    


if __name__ == '__main__':
    main()


