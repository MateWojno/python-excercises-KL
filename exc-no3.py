# while loop to get input x0,y0 is position of the queen x1, y1 is position of the desired move, input validation could be better but i think it is not about perfection.
while True:
    try:
        x0 = int(input('Give me x position of your queen from 1-8: '))
        y0 = int(input('Give me y position of your queen from 1-8: '))
        x1 = int(input('Give me x position of your queen move from 1-8: '))
        y1 = int(input('Give me y position of your queen move from 1-8: '))
    except ValueError or Exception or x0 ==0 or x0 > 8 or y0 == 0 or y0 > 8 or x1 == 0 or x1 > 8 or y1 ==0 or y1 > 8:
        print("Invalid input, try again")
    break


try:
    # if you want to move left and right all i need to check if the y0 and y1 (in my point of view it is a vertical axis) is the same
    if     x0 != x1 and y0 == y1:
        print ("YES")
    # if you want to move up and down all i need to check if the x0 and x1 (in my point of view it is a horizontal axis) is the same
    elif   y0 != y1 and x0 == x1:
        print ("YES")
    # if both x0,x1 y0,y1 are the same there is no move
    elif   x0 == x1 and y0 == y1:
        print("There is no move needed")
    # if you want to move diagonally i figured out this idea, imo it is very simple to use and compute
    # for moving diagonally right up and left down (sum of x0 and y0) is equal (sum of x1 and y1)
    # for moving the other way diagonally it is all about subtraction from origin so (x0-x1) distance is equal as (y0-y1)
    elif   x0 + y0 == x1 + y1 or x0 - x1 == y0 - y1:
        print("YES")
    else:
        print("NO")
    # this exception is unfinished but it should not perform the operations above if input is invalid
except ValueError:
    if x0 == 0 or x0 > 8 or y0 == 0 or y0 > 8 or x1 == 0 or x1 > 8 or y1 == 0 or y1 > 8:
        print("This can't be done")
    # MateWojno 
