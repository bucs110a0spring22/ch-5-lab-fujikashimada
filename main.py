import turtle
import random
import time

#draws the grid for the graph. 
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.down()
  for i in range (4):
    myturtle.forward(width)
    myturtle.right(90)
  myturtle.up()

#draws the lines on the graph.
def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.goto(x_start, y_start)
  myturtle.down()
  myturtle.goto(x_end,y_end)
  myturtle.up()

#draws the circle for the dart board. 
def drawCircle(myturtle=None, radius=0, step=None):
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.circle(radius, 360, step)
  myturtle.up()

#sets up the dartboard. 
def setUpDartboard(myscreen=None, myturtle=None): 
  myturtle.color("black")
  turtle.setworldcoordinates(-2.5, -2.5, 2.5, 2.5)
  drawSquare(myturtle, 2, -1, 1)
  drawLine(myturtle=myturtle, x_start=-1.25, x_end=1.25)
  drawLine(myturtle=myturtle, y_start=1.25, y_end=-1.25)
  drawCircle(myturtle, 1, 100)

def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  if myturtle.distance(0,0)<=1:
    return True
  return isInCircle

#throwing darts at the dartboard. 
def throwDart(myturtle=None):  
  myturtle.goto(random.uniform(-1, 1), random.uniform(-1,1))
  myturtle.down()
  if isInCircle(myturtle, 0, 0, 1)==True:
    myturtle.color("green")
    myturtle.dot(3,"green")
    myturtle.up()
  else:
    myturtle.color("red")
    myturtle.dot(3,"red")
    myturtle.up()

#calculating scores and returing winner. 
def playDarts(myturtle=None):
  aPoints = 0
  bPoints = 0
  for i in range(10):
    throwDart(myturtle)
    if myturtle.color()[0]=="green":
      aPoints += 1  
    throwDart(myturtle)  
    if myturtle.color()[0]=="green":
      bPoints += 1
  print("Player A, your final score is:", aPoints,"Player B, your final score is:", bPoints)
  if aPoints > bPoints:
    print("Congrats player A! You win!")
  elif aPoints < bPoints:
    print("Congrats player B! You win")
  else:
    print("It's a tie.")
  
#drawing a smiley face for the winner
def smilesForWinners(myturtle=None):
    myturtle = turtle.Turtle() 
    window = turtle.Screen()
    turtle.setworldcoordinates(-150, -150, 150, 150)
    def eye(color, radian):
      myturtle.down()
      myturtle.fillcolor(color)
      myturtle.begin_fill()
      myturtle.circle(radian)
      myturtle.end_fill()
      myturtle.up()
    # draw face
    myturtle.width(2)
    myturtle.fillcolor('yellow')
    myturtle.begin_fill()
    myturtle.circle(100)
    myturtle.end_fill()
    myturtle.up()
    # draw eyes
    myturtle.goto(-30, 115)
    eye('black', 5)
    myturtle.goto(30, 115)
    eye('black', 5)
    # draw mouth
    myturtle.goto(-35, 85)
    myturtle.down()
    myturtle.right(90)
    myturtle.circle(35, 180)
    myturtle.up()
    myturtle.clear()

#Calculating Pi by throwing number of darts called by the user. 
def montePi(myturtle=None, num_darts=0):
  insideCount = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if myturtle.color()[0]=="green":
      insideCount += 1
  approximatePi=insideCount/num_darts*4 
  return approximatePi

#asking user for birth year and returing their current age. 
def age(birth_year=0):
  current_year = 2022
  age = current_year - birth_year
  return age

def main():
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) 
    setUpDartboard(window, darty)

    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    smilesForWinners(darty)
    print("\tPart B Complete...")
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)

      # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)
 # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
  
    user_birth_year = int(input("\nPlease input the Year You Were Born In:")
    calculatedAge = age(user_birth_year)
    print("\nSince you were born in",     str(birth_year), "you are", str(calculatedAge), "years old")

    window.exitonclick()

main()
