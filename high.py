#!/usr/bin/env python
from __future__ import print_function
import xbox
from Arduino import Arduino
import time

# Define Arduino variables
servo1 = 9
servo2 = 6
servo3 = 5
servo4 = 3
servo5 = 11

board = Arduino()
board.Servos.attach(servo1)
board.Servos.attach(servo2)
board.Servos.attach(servo3)
board.Servos.attach(servo4)
board.Servos.attach(servo5)

angle1 = 90
angle2 = 90
angle3 = 90
angle4 = 90
angle5 = 0

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)

# Move servo with respect to the left analog stick X values limited to the min-max angle set 
def leftXmove(servonum,minAngle,maxAngle):
    angle = angle1
    if int(joy.leftX()) > 0:
        angle = angle - 2 
        if angle <= minAngle:
            angle = minAngle
        return angle
    elif int(joy.leftX()) < 0:
        angle = angle + 2
        if angle >= maxAngle:
            angle = maxAngle
        return angle
    else:
        return angle
    
# Move servo with respect to the left analog stick X values limited to the min-max angle set 
def leftYmove(servonum,minAngle,maxAngle):
    angle = angle2
    if int(joy.leftY()) > 0:
        angle = angle - 2
        if angle <= minAngle:
            angle = minAngle
        return angle
    elif int(joy.leftY()) < 0:
        angle = angle + 2
        if angle >- maxAngle:
            angle = maxAngle
        return angle
    else:
        return angle

# Move servo with respect to the right analog stick Y values limited to the min-max angle set     
def rightYmove(servonum,minAngle,maxAngle):
    angle = angle3
    if int(joy.rightY()) > 0:
        angle = angle - 2
        if angle <= minAngle:
            angle = minAngle
        return angle
    elif int(joy.rightY()) < 0:
        angle = angle + 2
        if angle >= maxAngle:
            angle = maxAngle
        return angle
    else:
        return angle

	
# Move servo with respect to the right analog stick X values limited to the min-max angle set     
def rightXmove(servonum,minAngle,maxAngle):
    angle = angle4
    if int(joy.rightX()) > 0:
        angle = angle - 2
        if angle <= minAngle:
            angle = minAngle  
        return angle
    elif int(joy.rightX()) < 0:
        angle = angle + 2
        if angle >= maxAngle:
            angle = maxAngle
        return angle
    else:
        return angle

# Move servo when right trigger is used
def rightTrigmove(servonum,minAngle,maxAngle):
    angle5 = minAngle
    if int(joy.rightTrigger()) > 0:
        angle5 = maxAngle
        board.Servos.write(servonum,angle5)
    else:
        board.Servos.write(servonum,minAngle)

# Instantiate the controller
joy = xbox.Joystick()

# Show various axis and button states until Back button is pressed
print("Xbox controller sample: Press Back button to exit")
while not joy.Back():
    # Show connection status
    show("Connected:")
    showIf(joy.connected(), "Y", "N")    
    # Left analog stick
    show("  Left X/Y:", fmtFloat(joy.leftX()), "/", fmtFloat(joy.leftY()))      
    # Right analog stick
    show("  Right X/Y:", fmtFloat(joy.rightX()), "/", fmtFloat(joy.rightY()))  
    # Right trigger
    show("  RightTrg:", fmtFloat(joy.rightTrigger()))
    # Poll controller leftX values and move servo1 accordingly
    angle1 = leftXmove(servo1,0,180)
    board.Servos.write(servo1,angle1)
    # Poll controller leftY values and move servo2 accordingly
    angle2 = leftYmove(servo2,0,120)
    board.Servos.write(servo2,angle2)
    # Poll controller rightY values and move servo3 accordingly
    angle3 = rightYmove(servo3,0,180)
    board.Servos.write(servo3,angle3)
    # Poll controller rightX values and move servo4 accordingly
    angle4 = rightXmove(servo4,0,180)
    board.Servos.write(servo4,angle4)
    # Move claw conencted to servo5 depending on right trigger value
    rightTrigmove(servo5,0,90)
    # A/B/X/Y buttons
    show("  Buttons:")
    showIf(joy.A(), "A")
    showIf(joy.B(), "B")
    showIf(joy.X(), "X")
    showIf(joy.Y(), "Y") 
    # Dpad U/D/L/R
    show("  Dpad:")
    showIf(joy.dpadUp(),    "U")
    showIf(joy.dpadDown(),  "D")
    showIf(joy.dpadLeft(),  "L")
    showIf(joy.dpadRight(), "R")  
    # Move cursor back to start of line
    show(chr(13))
# Close out when done
joy.close()
