from Tkinter import *
import time
from math import cos, sin, atan2, degrees, radians
import numpy as np

deg_90= -1.57079633

canv_width=600
canv_height=400

pole_length=2
pole_mass=8.0

g=9.81
time_step=0.1

def drawcircle(canv,x,y,rad):
    canv.create_oval(x-rad,y-rad,x+rad,y+rad,width=0,fill='blue')


class poleObj(object):

    def __init__(self,p1_x,p1_y,p2_x,p2_y,angle,angular_velocity):
        #print "Creating pole"
        self.p1_x=p1_x
        self.p1_y=p1_y
        self.p2_x=p2_x
        self.p2_y=p2_y
        self.angle=angle
        self.angle_drawing=angle +deg_90
        self.rotate (angle)

        self.angular_speed=angular_velocity
        self.angular_acc=0.0
        self.length=pole_length
        self.mass=pole_mass


    def draw(self,canv):
        self.pole_draw = canv.create_line(self.p1_x, self.p1_y, self.p2_x, self.p2_y, fill='red')

    def move (self,canv,x,y):
        self.p1_x=self.p1_x+x
        self.p1_y=self.p1_y+y
        self.p2_x=self.p2_x+x
        self.p2_y=self.p2_y+y



    def rotate (self,theta):


        #self.angle_drawing=self.angle_drawing + theta
        #self.angle=self.angle+theta

        #original coordinates
        x_bak=self.p1_x
        y_bak=self.p1_y

        #move to origin
        self.p1_x=self.p1_x-x_bak
        self.p1_y=self.p1_y-y_bak
        self.p2_x=self.p2_x-x_bak
        self.p2_y=self.p2_y-y_bak

        #rotate
        self.p2_x=pole_length*70*cos(self.angle_drawing)
        self.p2_y=pole_length*70*sin(self.angle_drawing)

        #translate back
        self.p1_x=self.p1_x+x_bak
        self.p1_y=self.p1_y+y_bak
        self.p2_x=self.p2_x+x_bak
        self.p2_y=self.p2_y+y_bak

    def apply_noise(self):
        angle_noise=np.random.normal(0.0, 0.001)
        self.angle=self.angle+angle_noise

        angular_speed_noise=np.random.normal(0.0, 0.001)
        self.angular_speed=self.angle+angular_speed_noise




def part_7_1():
    print "part 7.1"

    initial_angle=0.3
    initial_speed=-0.5

    root = Tk()
    canv = Canvas(root, width=canv_width, height=canv_height)
    canv.pack(fill='both', expand=True)

    #Create objects
    pole = poleObj(canv_width/2, canv_height-200, canv_width/2, canv_height-200-pole_length, initial_angle, initial_speed) #point 1 x and y, point 2 x and y , angle and angular speed

    #Draw objects
    right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
    left = canv.create_line(0, 0, 0, canv_height, fill='red')

    pole.draw(canv)

    iters=0
    while iters < 300:
        time.sleep(time_step)
        canv.delete("all")


        #move the pendulum
        pole.angle=pole.angle+time_step*pole.angular_speed;
        pole.angle_drawing= pole.angle +deg_90
        #pole.angle_drawing=pole.angle_drawing +time_step*pole.angular_speed

        angle_acceleration=g/pole.length* sin(pole.angle);
        pole.angular_speed=pole.angular_speed+ time_step*angle_acceleration

        pole.rotate(pole.angle)


        #draw
        pole.draw(canv)
        right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
        left = canv.create_line(0, 0, 0, canv_height, fill='red')

        canv.update()
        iters=iters+1

    root.destroy()


def part_7_2():
    print "part 7.2"

    initial_angle=0.3
    initial_speed=-0.5

    root = Tk()
    canv = Canvas(root, width=canv_width, height=canv_height)
    canv.pack(fill='both', expand=True)

    #Create objects
    pole = poleObj(canv_width/2, canv_height-200, canv_width/2, canv_height-200-pole_length, initial_angle, initial_speed) #point 1 x and y, point 2 x and y , angle and angular speed

    #Draw objects
    right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
    left = canv.create_line(0, 0, 0, canv_height, fill='red')

    pole.draw(canv)

    iters=0
    while iters < 300:
        time.sleep(time_step)
        canv.delete("all")


        #Move
        s=np.array([pole.angle,pole.angular_speed])[:,None] #column vector for state
        A= np.matrix( ((1, 0.1), (0.1*g/pole.length,  1.0)) )
        B = np.matrix( ((0.0), (0.1)) ) [:,None]

        s=A*s ;

        #print "angle from matrix is", s.item (0,0)
        #print "speed from matrix is", s.item (1,0)

        pole.angle=s.item (0,0)
        pole.angle_drawing= pole.angle +deg_90
        pole.angular_speed=s.item (1,0)

        print "speed is", pole.angular_speed

        pole.rotate(pole.angle)


        #draw
        pole.draw(canv)
        right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
        left = canv.create_line(0, 0, 0, canv_height, fill='red')

        canv.update()
        iters=iters+1

    root.destroy()



def part_7_3():
    print "part 7.3"

    initial_angle=0.3
    initial_speed=-0.5

    root = Tk()
    canv = Canvas(root, width=canv_width, height=canv_height)
    canv.pack(fill='both', expand=True)

    #Create objects
    pole = poleObj(canv_width/2, canv_height-200, canv_width/2, canv_height-200-pole_length, initial_angle, initial_speed) #point 1 x and y, point 2 x and y , angle and angular speed

    #Draw objects
    right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
    left = canv.create_line(0, 0, 0, canv_height, fill='red')

    pole.draw(canv)


    U= np.matrix( ((1, 0.1), (0.1,  1.0)) )
    V=42


    iters=0
    while iters < 300:
        time.sleep(time_step)
        canv.delete("all")


        #Move
        s=np.array([pole.angle,pole.angular_speed])[:,None] #column vector for state
        A= np.matrix( ((1, 0.1), (0.1*g/pole.length,  1.0)) )
        B = np.matrix( ((0.0), (0.1)) ) [:,None]

        s=A*s ;

        pole.angle=s.item (0,0)
        pole.angle_drawing= pole.angle +deg_90
        pole.angular_speed=s.item (1,0)

        pole.rotate(pole.angle)


        #reward
        a=pole.angular_acc
        reward=-(s.transpose()*U*s + a*V*a)
        print "reward is", reward


        #draw
        pole.draw(canv)
        right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
        left = canv.create_line(0, 0, 0, canv_height, fill='red')

        canv.update()
        iters=iters+1

    root.destroy()

'''
def run_6_2_episode(k1,k2,k3,k4):


    root = Tk()
    canv = Canvas(root, width=canv_width, height=canv_height)
    canv.pack(fill='both', expand=True)


    #Create objects
    #cart = cartObj(250, canv_height-cart_height, 250+cart_width, canv_height,0.2)
    pole = poleObj(250+cart_width/2, canv_height-cart_height, 250+cart_width/2, canv_height-cart_height-pole_length, 0.2, -0.2) #point 1 x and y, point 2 x and y , angle and angular speed

    #Draw objects
    #middle = canv.create_line(canv_width/2, 0, canv_width/2, 640, fill='red')
    right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
    left = canv.create_line(0, 0, 0, canv_height, fill='red')

    cart.draw(canv)
    pole.draw(canv)

    iters=0
    total_reward=0

    while iters < 1000:

        time.sleep(time_step)

        canv.delete("all")

        #Move and rotate
        F=F_func(cart,pole,k1,k2,k3,k4)
        simulate_timestep(cart,pole,time_step,F)

        #print cart.position()

        #draw
        cart.draw(canv)
        pole.draw(canv)
        right = canv.create_line(canv_width, 0, canv_width, canv_height, fill='blue')
        left = canv.create_line(0, 0, 0, canv_height, fill='red')


        #noise
        #cart.apply_noise()
        #pole.apply_noise()


        #give rewards
        if pole.angle > -0.1 and pole.angle < 0.1 and cart.position() > -0.1 and cart.position() < 0.1:
            total_reward = total_reward +0
        else:
            total_reward = total_reward -1

        #check boundaries and critical angle
        hit=cart.check_border()
        if hit or abs(pole.angle) >0.8:
            total_reward=total_reward+ (-2* (N-iters) )
            root.destroy()
            return total_reward

        canv.update()
        iters=iters+1



    total_reward=total_reward+ (-2* (N-iters) )
    root.destroy()
    return total_reward
'''



if __name__ == "__main__":

    #part_7_1()
    #part_7_2()
    part_7_3()


    #main()
