import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 2) or is_args_all_num(arguments) or not arguments[0].endswith(".txt") or not arguments[1].endswith(".txt")):
    error_case()
    
#Get the matrix from the file
def get_matrix(file_name):
    file_content = get_file_content(file_name)
    tab = []
    
    #Making a string line as an array
    if file_content != None:        
        for line in file_content:
            tab_line = []
            for char in line:          
                if('\n' not in char): #Don't take the \n 
                    if char.isspace() :
                        tab_line.append('-')
                    else:
                        tab_line.append(int(char))
            tab.append(tab_line)
                
    return tab    

#print properly a matrix
def matrix_to_string(matrix):
    for i in range(len(matrix)):
        ligne = ""
        for j in range (len(matrix[i])):
            ligne += str(matrix[i][j])
        print(ligne)
        
#Open the file and give the text inside
def get_file_content(file_name):
    try:
        file = open(file_name, 'r')
    except OSError:
        print('cannot open', file_name)
        error_case()
    else:
        result = file.readlines()
        file.close()
        return result
    
#Explore the double matrix to find a pattern 
def find_pattern(board, pattern):
    coord_found = ('-','-')
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            #Check first element is same and allow the pattern inside the board by the dimensions
            if (board[i][j] == pattern[0][0] and len(pattern[0]) + j <= len(board[i]) and len(pattern) + i <= len(board)):
                if check_inside(board, pattern, (i,j)):
                    coord_found = i, j
                    return coord_found
                else:
                    continue 
                    
    return coord_found

#Reveal if the pattern is inside the board using the coordinate association 
def check_inside(board, pattern, coord):
    for x in range(0, len(pattern)):
        for y in range(0, len(pattern[x])):
            if (board[coord[0] + x][coord[1] + y] != pattern[x][y] and pattern[x][y] != '-'):
                return False
        
    return True

#Get the board matrix with only the pattern visible
def pattern_in_board(board, pattern, coord):
    matrix_negative = [ ['-']*len(board[0]) for i in range(len(board))]
    
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            x = coord[0] + i
            y = coord[1] + j            
            matrix_negative[x][y] = pattern[i][j]
                        
    return matrix_negative

#Display in function of the coordinates found
def display_result(coord_found):
    if (coord_found != ('-','-')):    
        matrix_negative = pattern_in_board(board_matrix, to_find_matrix, coord_found)
        print("Trouvé")
        print("Coordonnées : ", coord_found)
        matrix_to_string(matrix_negative)
    else:
        print("Introuvable")

#Get the name of the files 
board_filepath = arguments[0]
to_find_filepath = arguments[1]

#Get the content of the file 
board_matrix = get_matrix(board_filepath)
to_find_matrix = get_matrix(to_find_filepath)

#Get the coordinates if found 
coord_found = find_pattern(board_matrix, to_find_matrix) 

#Display the result depending on the coordinate 
display_result(coord_found)