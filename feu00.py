import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or not is_pos_num(arguments[0]) or            #2 args, 2 positives numbers
    not is_pos_num(arguments[1]) or arguments[0] == "0" or arguments[1] == "0"): #Never equal to 0
    error_case()


def make_rectangle(x, y):
    rectangle = "o"
    
    
    for i in range(x - 2):
        rectangle += "-"
    
    return rectangle

#Get the arguments values
coordonnees_x = arguments[0]
coordonnees_y = arguments[1]

