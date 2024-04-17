"""
Galaga

Tyler Cloutier

What elements this project used:
 variables
 if statement
 complex bollean condition (and/or/not)
 Getting input from the user
 Printing output to the console
 One of the following operators //, %, +=, or -=
 Nested if-statement
 While loop
 For loop
 a graphics window
 a graphics animation
 uses a random number
 docstring for each function
 global variable
 local variables
 List
 Uses a custom class to create cutsom objects
 Changes an attribute of a custom object
"""
from graphics import *
import random
import time
from time import sleep

score = 0

class Game:
    
    def __init__(self, window):
        """
        Sets all the initial shapes in the window
        
        Parameter:
            window: passing through the Graphics Window to draw the shapes
        """
    
        self.window = window
        self.rect = Rectangle(Point(225, 475), Point(275, 450))
        self.rect.setFill("black")
        self.xspeed = 0
        self.yspeed = 3
        self.rect.draw(self.window)
        
        self.x = random.randint(50, 450)
        self.y = 70
    
        self.circ = Circle(Point(self.x,self.y), 10)
        self.circ.setFill("red")
        self.circ.draw(self.window)
        
        self.bar = Rectangle(Point(0,0), Point(500, 60))
        self.bar.setFill("light blue")
        self.bar.setOutline("light blue")
        self.bar.draw(self.window)
        
        self.score = Text(Point(460,30), "0")
        self.score.setSize(30)
        self.score.setTextColor("black")
        self.score.draw(self.window)
        
        self.life = Text(Point(30, 30), "3")
        self.life.setSize(30)
        self.life.setTextColor("black")
        self.life.draw(self.window)
        
                          
    
    def bullet_create(self):
        """
        Creates a bullet in the middle of the ship
        """
        self.cp1x = self.rect.getP1().getX()
        self.shot_x = self.cp1x + 25
        self.orb_speed = -15
        
        self.orb = Circle(Point(self.shot_x, 445), 5)
        self.orb.setFill("yellow")
        self.orb.draw(self.window)
        return self.orb
    
    def projectile_reset(self):
        """
        Undraws the moving projectile and resets its position at the top of the window
        
        Returns:
            self.circ: the shape and position of the projectile
        """
        self.x = random.randint(50, 450)
        self.circ.undraw()
        self.circ = Circle(Point(self.x, 70), 10)
        self.circ.setFill("red")
        self.circ.draw(self.window)
        return self.circ
    
    def bullet_update(self, bull_list):
        """
        Handles moving the individual bullets and undraws them when they reach a certain Y level
        
        Parameters:
            bullet_list: a list of the amount of bullets to update when the user press S
        """
        for bull in bull_list:
            if bull.getCenter().getY() > 65:
                bull.move(0, -15)
            else:
                bull.undraw()
                bull_list.remove(bull)
        
    
    def update(self):
        """
        Handles moving of the projectile
        """
        self.circ.move(self.xspeed, self.yspeed)
    
def collision(proj, shot):
    """
    Returns True of False for when the bullet collides with a projectile
    
    Parameters:
        proj: passing the projectile's shape through the function
        shot: passing the bullet's shape through the function
    
    Returns:
        True: the outcome is true when the two objects collide
        False: the outcome is false when the two objects do not collide
    """
    cp1x = proj.getP1().getX()
    cp1y = proj.getP1().getY()
    cp2x = proj.getP2().getX()
    cp2y = proj.getP2().getY()
    
    ap1x = shot.getP1().getX()
    ap1y = shot.getP1().getY()
    ap2x = shot.getP2().getX()
    ap2y = shot.getP2().getY()
        
    if cp2x > ap1x and cp1x < ap2x:
        if cp2y > ap1y and cp1y < ap2y:
            return True
    
    else:
        return False
        
    
        
def main():
    """
    Runs the Graphics Window
    
    Returns:
        score: the number of points the player accumulated
    """
    win = GraphWin("Awesome Game", 500, 500, autoflush=False)
    b = Game(win)
    ship = b.rect
    projectile = b.circ
    shot_T = False
    
    points = 0
    life_points = 3
    
    bullet_list = []
        
    while win.isOpen():
        key = win.checkKey()
        b.update()
        
        if ship.getCenter().getX() < 475:
            if ship.getCenter().getX() > 25:
                if key == 'Right':
                    ship.move(25, 0)
                elif key == 'Left':
                    ship.move(-25, 0)

            else:
                ship.move(5, 0)
        else:
            ship.move(-5, 0)
            
        if projectile.getCenter().getY() > 470:
            projectile = b.projectile_reset()
            life_points -= 1
            b.life.setText(life_points)
            
        if key == "s":
            bullet_list.append(b.bullet_create())
            b.bullet_update(bullet_list)
            shot_T = True
                
        if shot_T == True:
            b.bullet_update(bullet_list)
            for bullet in bullet_list:
                if collision(projectile, bullet) == True:
                    projectile = b.projectile_reset()
                    bullet.undraw()
                    points += 1
                    b.score.setText(points)
                    shot_T = False
        if life_points == 0:
            win.close()
            return points
        
        update(60)       
      
print(
"""Do you want to play a terrible version of Galaga? Here are the rules:
1. Press the Right and Left arrow keys to move your ship (the rectangle at the bottom of the screen)
2. Press S to fire your bullets at the oncoming astroids (the circles moving down the screen)
3. You get one point per astroid you destroy
4. You have 3 life points, and every time an astroid passes your ship, you lose one life point
5. When your life points reach 0, that's game over""")
main()
user = input("So, do you want to play?(yes/no) ")

if user == "yes":
    score = main()
    print("Nice! You got", score, "points!")
    
else:
    print("Maybe next time")

