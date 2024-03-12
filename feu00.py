import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or not is_pos_num(arguments[0]) or            #2 args, 2 positives numbers
    not is_pos_num(arguments[1]) or arguments[0] == "0" or arguments[1] == "0"): #Never equal to 0
    error_case()

#Return a string that make a rectangle with x : width and y : heigth
def make_rectangle(x, y):
    rectangle_line = "o"
    rectangle_column = "|"
    coord_x_tmp = x 
    
    #Making the line string 
    if (x > 1):
        while coord_x_tmp != 2:   #2 because of the 2 "o" before and after in the string 
            rectangle_line += "-"
            coord_x_tmp -= 1            
        rectangle_line += "o"
    
    #Making the collumn string
    if (y > 2 and x > 1):
        rectangle_column += " " * (x - 2)        
        rectangle_column += "|\n"
    
    #Adding lines and columns to make full rectangle
    rectangle_full = ""
    if  (y > 1 and x > 1):  #Ok to make any rectangle y>1 and x>1 even horizontal lines
        rectangle_full = rectangle_line + "\n" + rectangle_column * (y - 2) + rectangle_line
    elif(x == 1 and y > 1): #To make vertical lines
        rectangle_full = rectangle_line + "\n" + (rectangle_column + "\n") * (y - 2) + rectangle_line 
    else:
        rectangle_full = rectangle_line #For the x : 1 and y : 1 case
        
    return rectangle_full

#Get the arguments values
coordonnees_x = int(arguments[0])
coordonnees_y = int(arguments[1])

print(make_rectangle(coordonnees_x, coordonnees_y))