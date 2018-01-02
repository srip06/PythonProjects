import turtle
import math
#LINE CLASS

class line(object):

    def __init__(self,starting_position,ending_position,pensize,color):
        self.sp = starting_position
        self.ep = ending_position
        self.color = color
        self.ps = pensize

    def __str__(self):
        print str(self.sp)+" "+str(self.ep)+" "+str(self.color)

    def draw(self):
        turtle.penup()
        turtle.setposition(self.sp)
        turtle.pendown()
        turtle.pensize(self.ps)
        turtle.color(self.color)
        turtle.goto(self.ep)
        turtle.penup()


#RECTANGLE CLASS

class rectangle(object):

    def __init__(self,left_up,right_up,right_down,left_down,pensize,color):
        self.lu = left_up
        self.ru = right_up
        self.ld = left_down
        self.rd = right_down
        self.color = color
        self.ps = pensize

    def __str__(self):
        print str(self.lu)+" "+str(self.ru)+" "+str(self.ld)+" "+str(self.rd)+" "+str(self.ps)+" "+str(self.color)

    def draw(self):
        turtle.color(self.color)
        turtle.begin_fill()
        f1 = line(self.lu,self.ru,self.ps,self.color)
        f1.draw()
        f2 = line(self.ru,self.rd,self.ps,self.color)
        f2.draw()
        f3 = line(self.rd,self.ld,self.ps,self.color)
        f3.draw()
        f4 = line(self.ld,self.lu,self.ps,self.color)
        f4.draw()
        turtle.end_fill()

#CIRCLE CLASS

class circle(object):

    def __init__(self,center_position,radius,pensize,b_color,f_color):
        self.cp = center_position
        self.r = radius
        self.ps = pensize
        self.b_color = b_color
        self.f_color = f_color

    def __str__(self):
        print self.cp


    def draw(self):
        turtle.penup()
        turtle.setposition(self.cp)
        turtle.pendown()
        turtle.pensize(self.ps)
        turtle.begin_fill()
        turtle.pencolor(self.b_color)
        turtle.fillcolor(self.f_color)
        turtle.circle(self.r)
        turtle.end_fill()

#TRIANGLE CLASS

class triangle(object):

    def __init__(self,current_position,top_position,end_position,pensize,b_color,f_color):
        self.edge1 = current_position
        self.edge2 = top_position
        self.edge3 = end_position
        self.ps = pensize-1
        self.b_color = b_color
        self.f_color = f_color

    def __str__(self):
        print str(self.edge1)+" "+str(self.edge2)+" "+str(self.edge3)+" "+str(self.ps)

    def draw(self):
        turtle.begin_fill()
        turtle.pencolor(self.b_color)
        turtle.fillcolor(self.f_color)
        turtle.right(120)
        turtle.goto(self.edge2)
        turtle.right(120)
        turtle.goto(self.edge3)
        turtle.right(120)
        turtle.goto(self.edge1)
        turtle.end_fill()


#SNOW PERSON CLASS
class snow_person(circle):
    np1 = ()
    np2 = ()
    np3 = ()
    def __init__(self,starting_position,r1,r2,r3,pen_size,b_color,f_color):
        self.sp = starting_position
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.ps = pen_size
        self.b_color = b_color
        self.f_color = f_color

    def __str__(self):
        print self.sp

    def drawing_3_circles(self):
        c1 = circle(self.sp,self.r1,self.ps,self.b_color,self.f_color)
        c1.draw()
        turtle.penup()
        self.np1 = (self.sp[0],self.sp[1]+(2*self.r1))
        turtle.goto(self.np1)
        c2 = circle(self.np1,self.r2,self.ps,self.b_color,self.f_color)
        c2.draw()
        turtle.penup()
        self.np2 = (self.np1[0],self.np1[1]+(2*self.r2))
        turtle.goto(self.np2)
        c3 = circle(self.np2,self.r3,self.ps,self.b_color,self.f_color)
        c3.draw()
        turtle.penup()
        self.np3 = (self.np2[0],self.np2[1]+(2*self.r3))
        
        

#CREATING SNOW MAN

class snow_man(snow_person):

    def __init__(self,sp,radius,pensize,b_color,f_color):
        self.np3 = sp.np3
        self.np2 = sp.np2
        self.np1 = sp.np1
        self.r = radius
        self.ps = pensize
        self.r3 = sp.r3
        self.r2 = sp.r2
        self.r1 = sp.r1
        self.b_color = b_color
        self.f_color = f_color

    def __str__(self):
        print str(self.np3)+" "+str(self.np2)+" "+str(self.np1)+" "+str(self.r2)

    def draw_small_circles(self,eye_color,first_circle_color,second_circle_color):
        turtle.penup()
        #FACE OF SNOW_MAN
        #LEFT EYE
        sm_c1 = self.np3[0]-(self.r3)/3,self.np3[1]-self.r3
        turtle.goto(sm_c1)
        print sm_c1,self.r3
        c4 = circle(sm_c1,self.r,self.ps,self.b_color,eye_color)
        c4.draw()
        turtle.penup()
        #RIGHT EYE
        sm_c2 = self.np3[0]+(self.r3)/3,self.np3[1]-self.r3
        turtle.goto(sm_c2)
        turtle.pendown()
        c5 = circle(sm_c2,self.r,self.ps,self.b_color,eye_color)
        c5.draw()
        
        #MIDDLE CIRCLE OF SNOW_MAN
        turtle.penup()
        turtle.setposition(self.np2)
        print "self.np2"+str(self.np2),str(self.r2)
        #TOP CIRCLE IN THE MIDDLE CIRCLE OF SNOW PERSON
        circle_1_pos = self.np2[0],self.np2[1]-(self.r2-(self.r2/4))
        #turtle.goto(-100,100)
        print "circle_1_pos"+str(circle_1_pos)
        turtle.goto(circle_1_pos)
        turtle.pendown()
        c6 = circle(circle_1_pos,(self.r+(self.r/2)),self.ps,self.b_color,first_circle_color)
        c6.draw()
        #DOWN CIRCLE IN THE MIIDLE CIRCLE OF SNOW PERSON
        circle_2_pos = self.np2[0],self.np2[1]-(self.r2+((self.r2)/2))
        print "circle_2_pos",str(circle_2_pos)
        turtle.penup()
        turtle.goto(circle_2_pos)
        turtle.pendown()
        c7 = circle(circle_2_pos,(self.r+(self.r/2)),self.ps,self.b_color,second_circle_color)
        c7.draw()
        #BOTTOM OF THE SNOW PERSON
        turtle.penup()
        turtle.setposition(self.np1)
        print "self.np1"+str(self.np1),str(self.r1)
        #TOP CIRCLE IN THE BOTTOM CIRCLE OF SNOW PERSON
        circle_3_pos = self.np1[0],self.np1[1]-(self.r1-(self.r1/4))
        #turtle.goto(-100,100)
        print "circle_3_pos"+str(circle_3_pos)
        turtle.goto(circle_3_pos)
        turtle.pendown()
        c8 = circle(circle_3_pos,(2*self.r),self.ps,self.b_color,first_circle_color)
        c8.draw()
        #DOWN CIRCLE IN THE BOTTOM CIRCLE OF SNOW PERSON
        circle_4_pos = self.np1[0],self.np1[1]-(self.r1+((self.r1)/2))
        print "circle_4_pos",str(circle_4_pos)
        turtle.penup()
        turtle.goto(circle_4_pos)
        turtle.pendown()
        c9 = circle(circle_4_pos,(2*self.r),self.ps,self.b_color,second_circle_color)
        c9.draw()
        
    def draw_mouth(self,color):
        #MIDDLE MOUTH POSITION
        mp1 = self.np3[0]+(self.r3)/3,self.np3[1]-(self.r3+(self.r3/2))
        mp2 = self.np3[0]-(self.r3)/3,self.np3[1]-(self.r3+(self.r3/2))
        turtle.penup()
        #turtle.goto(mp1)
        l1 = line(mp2,mp1,self.ps,color)
        l1.draw()
        #RIGHT MOUTH POSITION
        mrp = self.np3[0]+((self.r3))/1.8,self.np3[1]-(self.r3+self.r3/3)
        l2 = line(mp1,mrp,self.ps,color)
        l2.draw()
        #LEFT MOUTH POSITION
        turtle.penup()
        turtle.goto(mp2)
        mlp = self.np3[0]-((self.r3))/1.8,self.np3[1]-(self.r3+self.r3/3)
        turtle.pendown()
        l3 = line(mp2,mlp,self.ps,color)
        l3.draw()
        
    def draw_hat(self,color):
        #HAT
        hat_left_top_pos = self.np3[0]-(self.r1/2),self.np3[1]-(self.r1/10)
        hat_right_top_pos = self.np3[0]+(self.r1/2),self.np3[1]-(self.r1/10)
        hat_right_bottom_pos = self.np3[0]+(self.r1/2),self.np3[1]-(self.r1/6)
        hat_left_bottom_pos = self.np3[0]-(self.r1/2),self.np3[1]-(self.r1/6)
        turtle.penup()
        turtle.goto(hat_left_top_pos)
        r1 = rectangle(hat_left_top_pos,hat_right_top_pos,hat_right_bottom_pos,hat_left_bottom_pos,self.ps,color)
        r1.draw()
        top_hat_left_bottom_pos = self.np3[0]-(self.r1/4),self.np3[1]-(self.r1/10)
        top_hat_left_top_pos = self.np3[0]-(self.r1/4),self.np3[1]+(self.r1/2)
        top_hat_right_top_pos = self.np3[0]+(self.r1/4),self.np3[1]+(self.r1/2)
        top_hat_right_bottom_pos = self.np3[0]+(self.r1/4),self.np3[1]-(self.r1/10)
        turtle.penup()
        turtle.goto(top_hat_left_top_pos)
        turtle.pendown()
        r2 = rectangle(top_hat_left_top_pos,top_hat_right_top_pos,top_hat_right_bottom_pos,top_hat_left_bottom_pos,self.ps,color)
        r2.draw()

    def draw_hands(self,color):
        #HANDS FOR SNOW MAN
        #LFT HAND
        
        left_hand_starting_pos = self.np2[0]-(self.r2*2/3),self.np2[1]-(self.r2*3/4)
        left_hand_ending_pos = self.np2[0] - (2.3*self.r2), self.np2[1]-(self.r2/2)
        turtle.penup()
        turtle.setposition(left_hand_starting_pos)
        turtle.pendown()
        l4 = line(left_hand_starting_pos,left_hand_ending_pos,(2*self.ps),color)
        l4.draw()
        #RIGHT HAND
        right_hand_starting_pos = self.np2[0]+(self.r2*3/4),self.np2[1]-(self.r2*3/4)
        right_hand_ending_pos = self.np2[0] + (2*self.r2), self.np2[1]+(self.r2/9)
        turtle.penup()
        turtle.setposition(right_hand_starting_pos)
        turtle.pendown()
        l5 = line(right_hand_starting_pos,right_hand_ending_pos,(2*self.ps),color)
        l5.draw()

    
        
#SNOW LADY CLASS

class snow_lady(snow_man,snow_person):
    def __init__(self,sp,sm,radius,pensize,b_color,f_color):
        self.np3 = sp.np3
        self.np2 = sp.np2
        self.np1 = sp.np1
        self.r = radius
        self.ps = pensize
        self.b_color = b_color
        self.f_color = f_color
        self.r3 = sp.r3
        self.r2 = sp.r2
        self.r1 = sp.r1
        
    def __str__(self):
        pass

    def draw_mouth(self,color):
        #MIDDLE MOUTH POSITION
        mp1 = self.np3[0]+(self.r3)/3-2,self.np3[1]-(self.r3+(self.r3/2))-2
        mp2 = self.np3[0]-(self.r3)/3+2,self.np3[1]-(self.r3+(self.r3/2))-2
        mouth_radius = math.sqrt(((mp1[0]-mp2[0])*(mp1[0]-mp2[0]))+((mp1[1]-mp2[1])*(mp1[1]-mp2[1])))/2
        turtle.penup()
        #turtle.goto(mp1)
        turtle.right(90)
        c1 = circle(mp2,mouth_radius,self.ps,color,color)
        c1.draw()
        #RIGHT MOUTH POSITION
        mrp = self.np3[0]+((self.r3))/1.8,self.np3[1]-(self.r3+self.r3/3)
        l2 = line(mp1,mrp,self.ps+1,color)
        l2.draw()
        #LEFT MOUTH POSITION
        turtle.penup()
        turtle.goto(mp2)
        mlp = self.np3[0]-((self.r3))/1.8,self.np3[1]-(self.r3+self.r3/3)
        turtle.pendown()
        l3 = line(mp2,mlp,self.ps+1,color)
        l3.draw()

    def draw_hands(self,color):
        #HANDS FOR SNOW LADY
        #LFT HAND
        left_hand_starting_pos = self.np2[0]-(self.r2*2/3),self.np2[1]-(self.r2*3/4)
        left_hand_ending_pos = self.np2[0] - (2.3*self.r2), self.np2[1]-(self.r2/2)
        turtle.penup()
        turtle.setposition(left_hand_starting_pos)
        turtle.pendown()
        l4 = line(left_hand_starting_pos,left_hand_ending_pos,(2*self.ps),color)
        l4.draw()
        #RIGHT HAND
        right_hand_starting_pos = self.np2[0]+(self.r2*3/4),self.np2[1]-(self.r2*3/4)
        right_hand_ending_pos = self.np2[0] + (2*self.r2)+3, self.np2[1]-(self.r2)
        turtle.penup()
        turtle.setposition(right_hand_starting_pos)
        turtle.pendown()
        l5 = line(right_hand_starting_pos,right_hand_ending_pos,(2*self.ps),color)
        l5.draw()
        edge = self.np1[0]+(self.r1*3)/5,self.np1[1]-self.r1/10
        l6 = line(right_hand_ending_pos,edge,(2*self.ps),color)
        l6.draw()

    def draw_lady_hat(self):
        hat_starting_pos = self.np3[0]-(self.r3),self.np3[1]-(self.r3/10)
        turtle.penup()
        turtle.goto(hat_starting_pos)
        turtle.right(90)
        turtle.pendown()
        hat_top_pos = self.np3[0],self.np3[1]+(self.r3+self.r3/2)
        hat_ending_pos = self.np3[0]+(self.r3),self.np3[1]-(self.r3/10)
        t = triangle(hat_starting_pos,hat_top_pos,hat_ending_pos,self.ps-1,self.f_color,"yellow")
        t.draw()
        l1_pos = self.np3[0]-(self.r3-(self.r3/4)),self.np3[1]-(self.r3/10)
        turtle.goto(l1_pos)
        turtle.left(70)
        turtle.forward(self.r3*1.5)
        turtle.backward(self.r3*1.5)
        turtle.left(110)
        turtle.forward(6)
        turtle.right(110)
        turtle.forward(self.r3)
        turtle.backward(self.r3)
        turtle.left(110)
        turtle.forward(self.r3+2)
        turtle.right(70)
        turtle.forward(self.r3)
        turtle.backward(self.r3)
        turtle.left(70)
        turtle.forward(6)
        turtle.right(70)
        turtle.forward(self.r3*1.5)

    
def main():
    turtle.Screen()
    sp =snow_person((-100,-100),70,50,30,2,"black","")
    sp.drawing_3_circles()

    sm = snow_man(sp,5,2,"black","grey")
    sm.__str__()
    sm.draw_small_circles("blue","grey","grey")
    sm.draw_mouth("red")
    sm.draw_hat("darkred")
    sm.draw_hands("darkred")
    print turtle.position()
    
    sp1 =snow_person((100,-100),70,50,30,2,"black","")
    sp1.drawing_3_circles()  

    sl = snow_lady(sp1,sm,5,2,"black","darkred")
    sl.draw_small_circles("green","yellow","purple")
    sl.draw_mouth("red")
    sl.draw_hands("darkred")
    sl.draw_lady_hat()
      
    turtle.exitonclick()

main()






