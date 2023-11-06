
#Question 1 - Hill Climbing :
#a. Consider a function f(x) = 2 - x2in the following
# discrete state-space, where x ∈ [-5, 5] , step-size 0.5
#Implement hill climbing algo. to find max value of function

#b.Change the step-size to 0.01.
#Run the hill-climbing algorithm and share your observations.


def f(x): #the function
  return 2 - x**2

def hill_climbing(step_size, current_x):


  while True:
    current_y = f(current_x) #getting the current y value from the given x
    neighbor = [f(current_x + step_size), f(current_x - step_size)]
    max_neighbor = max(neighbor) #max() returns the highest

    if max_neighbor <= current_y:
      break #this will break if the max is equal or less cause
            #that's not the maximum way anymore

    if neighbor[0] == max_neighbor:
     current_x += step_size #change the x value depending on the correlation
     #of the neighbor(0) and the max_neighbor value
    else:
      current_x -= step_size

  return current_x

#test cases for different step sizes
x = hill_climbing(.5,5)
print("Using the step-size .5:")
print("Max value found:", f(x))
print("x value:", x)

print("Using the step-size .01:")
x1 = hill_climbing(.01,5)
print("Max value found:", f(x1))
print("x value:", x1)
