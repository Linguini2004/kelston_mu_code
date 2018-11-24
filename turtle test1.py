import turtle as t
number_intresting = False
n = 1
factors = 0

t.setup(width = 1500, height = 200, startx = 0, starty = 100)

t.penup()
t.setposition(-490,0)
t.pendown()

def intresting(n):
    factors = 0 
    for divider in range(100):
        divider += 1
        remainder = n % divider
        if remainder == 0:
            factors += 1
    if factors == 2:
         return True 
    else:
        return False
     
def polygon(n_sides):
    for i in range(n_sides):
        t.forward(10)
        t.left(360.0 / n_sides)
        

def line():
    t.forward(10)
    
for i in range(1,100):
    number_intresting = intresting(i)
    if number_intresting:
        polygon(4)  
        t.forward(10)
    else:
        line()

