
'''-------------CONFETTI- Bursting of shapesssssssssss,wohooooooooooo------------------ '''


''' MAKE THE CONFETTI BOUNCE USING BOUNCE BALL PHYSICS HERE DOWN  '''
        
'''||||||||||||||||||||||||||||||||||||  '''   
'''VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV  '''   
                
                
                
                
def setup():
    size(640,360)
    
    global t, msg, count
    
    # starting msg on screen
    msg = "Click anywhere to burst..."
    t = "{t}" .format(t = msg)
    
    # count meter to manage the memory
    count = 0
    
    # initializing a main_list to hold all the bursts (each burst is a list of confettis)
    global all_bursts
    all_bursts = []
    
        
# mousePressed event
def mousePressed():
    
    global t, count
    
    
    # Creating a new_list of bursts when mousepressed
    new_burst = []
    
    # for all the objs in the list, when mousePressed, 'x' 'y' values updates
    for i in range(50):
        c = Confetti()
        c.burst(mouseX, mouseY)
        # all 'c' objs are stored in this list
        new_burst.append(c)
    
    # and then, appending new_burst in main_list;   //to retain all the confettis
    all_bursts.append(new_burst)

    count +=1 
    
    t = " Press 'c' to clear screen..."
    print "count", count
    
    # assigning a limit for msg
    if count >5:
        t = " Now Clear, or PC will burst"
        


def draw():
    
    background(0)
    
    global t
    
    # text attributes
    fill(200)
    textSize(15)
    text(t, 10, 20)
    
    # when first clicked, msg changes
    # if mousePressed:
    #     t = " Press 'c' to clear screen..."
    
    
    
    # calling the funcs for every obj from the list in the lists
    for burst in all_bursts:
        for c in burst:
            c.update()
            c.show()
    



def keyPressed():
    
    global all_bursts, t, msg, count
    
    if key == 'c':
        all_bursts = []
        
        #  back to start msg, to start again
        t = "{t}" .format(t = msg)
        
        # start count again
        count = 0





" -------------------CONFETTI class-------------------------"

class Confetti(object):
    
    # constructor arguments
    def __init__(self):
        
        # toggle to control the visibility of confettis; Turns on only when mousePressed      //avoids the starting draw of the confettis
        self.active = False
        
        # assigning 'x' 'y' somewhere out of the screensize, so not to see them in start
        self.x = 0            
        self.y = 0
        # size 
        self.s = 15
        
        # falling speed
        self.x_speed = 0
        self.y_speed = 0
        
        # physics_variables
        self.gravity = 0.5        # downward force
        self.damping = 0.6        # factor for lose of energy after bounce ; Y direcn collision
        self.wall_damping = 0.8   # damping factor for X direcn collision
        
        # color
        self.clr = color( random(200) , random(200), random(200))
        
    # draws the confettis
    def show(self):
        
        # checking the toggle
        if self.active:
            fill(self.clr)
            noStroke()
            
            circle( self.x, self.y, self.s)
    
    # func that updates the x,y vals, and assigns speed when mousepressed
    def burst(self, mx, my):
        
        # Toggle on
        self.active = True
        # 'x' 'y' values of circles are assigned from mouseX and mouseY
        self.x = mx
        self.y = my
        
        # takes random values, feels natural
        self.x_speed = random(-8,8)
        self.y_speed = random(-5,5)
    
    
    # func that continously updates the 'x' 'y' speeds
    def update(self):
        
        
        # updating loc of circles with,  x & y speeds to make them burst
        self.x += self.x_speed
        self.y += self.y_speed 
        
        # this is done to make it fall to the ground as if gravity was exists; adds the 'y_speed' everytime in the draw loop
        self.y_speed += self.gravity
        
        # checking for collision and bounce
        self.checkbounce()
        
        
    """ Want to make the balls bounce as they hit on the floor.............JLOOOOOO """
    # func that checks if confettis hit the bottom_edge
    def checkbounce(self):
        
        """ Bottom Edge Bounce (Y-axis) """
        # as its a circle, check the bottom point of edge with wrt screen height
        if self.y >= height - (self.s/2):
            
            # snap to ground to prevent sinking
            self.y = height - (self.s/2)
            
            
            """ damping the energy """
            # multiplying with a neg factor, reverses the direcn and reduces the velocity,
            self.y_speed *= -self.damping
            # print self.y_speed
            
            # friction in 'x'
            self.x_speed *= 0.7
            
            # preventing the tiny long decimal numbers
            if abs(self.y_speed) < 0 :                        #### Need to workout this part; bounce doesnt stop
                # putting it to stop
                self.y_speed = 0
        
        
        """ Left Edge Bounce (X-axis) """
        if self.x <= self.s/2:
            
            # snapping to edge
            self.x = self.s/2
            
            # reverse and dampen
            self.x_speed *= -self.wall_damping
            
            if abs(self.x_speed) < 0.5:
                self.x_speed = 0
                
                
        """ Right Edge Bounce (X-axis) """
        if self.x >= width - (self.s/2):
            
            # snapping to edge
            self.x = width - (self.s/2)
            
            # reverse and dampen
            self.x_speed *= -self.wall_damping
            
            if abs(self.x_speed) < 0.5:
                self.x_speed = 0
                
        
        
            
        
        
        
