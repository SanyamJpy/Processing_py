''' ----------------------------------POPPINGGG BUBBLES for CONFETTIS---------------------------------------------'''

' can TRY THIS  ::::::>> if certain amt of bubbles missed, GAME OVER ;D'




def setup():
    size(900, 500)
    
    
    # global variables
    global bub, total_score, speed_Y, all_bursts, new_burst, start_msg_toggle
    
    start_msg_toggle = True   # Toggle for the opening msg
    speed_Y = 0               # initializing upward speed 
    total_score = 0           # initializing global score here
    bub =[]                   # list to hold bubbles
    
    # loop to add multiple bubbles for class Bubble()
    for _ in range(2):
        x = int(random(width))
        y = height
        bub.append(Bubble(x,y))
    
    print bub
    
    # cursor turns into hand
    cursor(HAND)
    
    
    # all_bursts = []   // dont need it, as we dont want to retain the confettis
    # List to take the confettis from popped bubbles
    new_burst = []
    
    
    
def draw():
    background(255)
    
    global speed_Y
    
    # while mouse is not pressed, show this msg
    if start_msg_toggle:
        start_msg = "Click on Bubbles to Pop :D"
        fill(10,90,180)
        textSize(30)
        text(start_msg, (width/2-150), (height/2))
    
    # if all bubbles popped; add bubbles
    if not bub:
        
        # delay between last popped bubble and new bubbles, // although not so imp 
        # delay(50)
        
        # adding random no of bubbles in list
        for _ in range(int(random(2,6))):
            print _, "here"
            x = int(random(width))
            y = height
            bub.append(Bubble(x,y))
        
        # after every iteration, speed increments
        speed_Y += 0.2
        

        
    # calling the funcns of the class for the instances; Drawing the bubbles
    for b in bub:
        b.update()
        b.show()

    # How many bubbles popped? ; displaying total score 
    fill(0)
    textSize(20)
    text( "Pop:{}".format(total_score), width-80, 20)
    
    print speed_Y , "Speed y"
    
    # loop to draw confettis
    for c in new_burst:
        c.update()
        c.show()


# Mousepressed event
def mousePressed():
    
    global total_score, new_burst, start_msg_toggle
    
    # as mouse is prsd, toggle off, msg off
    start_msg_toggle = False
    
    
    
    # checking if clicked inside a Bubble
    for b in bub:
         
         if (b.check(mouseX, mouseY)):
             # b. clr_change()
   
             
             # Removes the bubble
             bub.remove(b) 
             b.popping()
             
             # incrementing global score 
             total_score += 1 
             
             # NO popped confettis on screen: making list empty here again ensures that confettis dont retain on screen
             new_burst = []
             
             # Adding the confetti class for POP bubbles
             for i in range(10):
                 c = Confetti()
                 c.burst(mouseX, mouseY)
                 new_burst.append(c)
                 


" ------------------------------------------------Bubble class------------------------------------------------------------------------"




class Bubble(object):
    
    # instance variables
    def __init__(self, x, y):
        self.x = x                   # 'x' loc of bubble
        self.y = y                   # 'y' loc of bubble
        self.initial_y = y           # to store the value for resetting when bubble hits edge
        self.s = random (40,150)     # random size variable
        self.clr = color(random(10), 100, random(100) )   # random color variable
    
    
    
    # FUNC to move bubble in 'x' and 'y'
    def update(self):
        
        self.x = self.x + int(random(-2,2))                         # lil wiggling effect in 'x' direcn
        self.y = self.y - int(random(1,4) )                         # rising up in 'y' 
        
        # increment of upward speed after evert iteration
        self.y = self.y - speed_Y
        # print self.y
        
        # if bubble hits edge, y value resets to initial
        self.restart()
    
    
    
    # FUNC to reset the bubble when it hits the edge
    def restart(self):
        
        # setting the value to initial y val user enters
        if self.y < -self.s :
            self.y = self.initial_y
            self.clr = color(random(10), 100, random(100) )           # resets the color as well
            self.x = random(0, width)           # also gives a new 'x' pos
             
             
             
    # FUNC to draw the bubbles
    def show(self):
        
        strokeWeight(3)
        # noFill()
        fill(self.clr)
        # background(255)
        
        circle(self.x, self.y, self.s)
        
        # a relection arc
        strokeWeight(4)
        stroke(255)
        
        arc(self.x, self.y, self.s -15, self.s-15, PI, 3*PI/2)
        
        
    
    # FUNC to check if you clicked on bubble
    def check(self, mx, my):
        
        # checks the dist b/w 'x''y' of circle and 'x''y' of where you mousePress
        d = dist (self.x, self.y , mx, my)
        
        # debug, for class COnfetti
        if d < self.s:
            print (self.x, "self.x")
            print (self.y, "self.y")
            
        # if its within the radius of bubble, then you hit it, otherwise not
        # returns true or false as per result
        return d < self.s/2
        
    # FUNC to simulates popping of bubble
    def popping(self):
        
        fill (0)
        t = "pop"
        textSize(20)
        text(t, self.x, self.y)
        
        
        
    # FUNC that changes color of bubble as you click on a bubble
    def clr_change(self):
        
        self.clr = color(random(255), 0, random(255) )
        
        
        

" ------------------------------------------------CONFETTI class------------------------------------------------------------------------"



class Confetti(object):
    
    # constructor arguments
    def __init__(self):
        
        # toggle to control the visibility of confettis; Turns on only when mousePressed      //avoids the starting draw of the confettis
        self.active = False
        
        # assigning 'x' 'y' as 0, so not to see them in start, but doesnt matter as toggle is False
        self.x = 0            
        self.y = 0
        # size 
        self.s = 5
        
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
        
        
        
        
        
        
        
