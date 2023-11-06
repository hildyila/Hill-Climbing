import random

#Random-restart hill-climbing
#Consider a function
#g(x) = (0.0051x5) - (0.1367x4) + (1.24x3) - (4.456x2) + (5.66x) - 0.287
#in the following discrete state-space, where x  [0, 10], step-size 0.5.
#Implement the random-restart hill-climbing algorithm for 20 random restarts
#in python to find the global maximum value for the above function.


def g(x):
  return (0.0051 * x**5) - (0.1367 * x**4) + (1.24 * x**3) - (4.456 * x**2) + (5.66 * x) - 0.287



def hill_climbing(step_size, current_x):


  while True:
    current_y = g(current_x) #getting the y value from the funciton input x
    neighbor = [g(current_x + step_size), g(current_x - step_size)]
    max_neighbor = max(neighbor) #max() returns the highest

    if max_neighbor <= current_y:
      break #this will break if the max is equal or less cause
            #that's not the maximum

    if neighbor[0] == max_neighbor:
     current_x += step_size
    else:
      current_x -= step_size
  y = g(current_x)

  return current_x, y



def random_restart_hill_climbing(num_restarts, step_size,ranges):

  #need to compare between each iterations so using these
  #variables to do that
  max = None
  max1 = None

  for i in range (num_restarts): #loop through the # of iterations

    x_pick = random.uniform(ranges[0],ranges[1])
    #choosing a random x between the ranges given
    x, y = hill_climbing(step_size,x_pick)
    #usign hill climbing algo to get the x and y of the max part in the area

    #this is where the comparison is between the iterations
    if (max is None) or (y > max): #if
      max = y
      max1 = x

  return x , y

#declaration of variables
restarts = 30
ranges = (0,10)
step_size = .5


#test cases
x_value , maximum = random_restart_hill_climbing(restarts,step_size,ranges)
print("Using Random-restart hill-climbing:")
print("x value:", x_value)
print("Max value:", maximum)


x_value1, maximum1 = hill_climbing(.5,0)
print("Using just hill climbing algorithm:")
print("x value:", x_value1)
print("max value:", maximum1)
