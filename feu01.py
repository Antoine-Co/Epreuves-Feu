import sys
from fonctions_annexes import *

#Get the array of args without the script name
arguments = sys.argv[1:]

#Check if the argument is well done
if (is_args_len_diff(arguments, 1)):
    error_case()

#Return array of char from a string 
def string_to_array(expression):
    tab = []
    for character in expression:
        tab.append(character)
    return tab

#Return the array with int, operator and parenthesis only
def clean_expr(expression):
    stack = []
    index = 0
    
    while index < len(expression):
        if (is_num(expression[index])):
            number = expression[index]
            index += 1
            while index < len(expression) and is_num(expression[index]):
                number += expression[index]
                index += 1
            stack.append(int(number))
            
        elif(is_operator(expression[index]) or expression[index] == '(' or expression[index] == ')'):
            stack.append(expression[index])
            index += 1
        else: 
            index += 1
            
    if(check_parenthesis(stack)):
        return stack
    else:
        error_case("Probleme dans les parenthèses")
    
#Return the array with negative number with parenthesis in int    
def set_negative_number(expression):
    index_to_del = []
    
    for i in range(len(expression)):
        if(expression[i] == '('): #Detection of negatives number like this (-9)
            if (i + 3 < len(expression) and expression[i + 1] == '-' and isinstance(expression[i + 2], int)
                and expression[i + 3] == ')'):
                expression[i] = - expression[i + 2]
                index_to_del.append(i + 1)
                index_to_del.append(i + 2)
                index_to_del.append(i + 3)
        
    for index in index_to_del[::-1]: #Reverse popin to have good index 
        expression.pop(index)
    
    return expression

#Check the number of parenthesis 
def check_parenthesis(expression):
    cpt_par = 0
    for character in expression:
        if (character == '('):
            cpt_par += 1
        elif (character == ')'):
            cpt_par -= 1 
    
    if(cpt_par == 0):
        return True 
    else:
        return False

#Steps to clean the string expression and then give an array with all tokens
def lexer(expression):
    array_expr = string_to_array(expression)
    expression_clean = clean_expr(array_expr)
    expression_clean_with_negatives = set_negative_number(expression_clean)
    return expression_clean_with_negatives
    
#Define the operator priority by a dictionnary
def priority(operator):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 3}
    return priority.get(operator)

#Check if its associative
def is_associative(operator):
    if (operator == '+' or operator == '*'):
        return True
    else:
        return False

#Check if a char is an operator 
def is_operator(character):
    if (character == '+' or character == '-' or character == '/' or character == '*' or character == '%'):
        return True 
    else:
        return False
    
#Convert the arithmetical expr in Reverse Polish Notation (RPN)
def shunting_yard(expression):
    #2 stacks one for the final result one for the operators/parenthesis
    stack_res = []
    stack_ope = []
    
    #Reading the expression from left to right
    for i in range(len(expression)):
        #The element is a number -> final stack
        if isinstance(expression[i], int):
            stack_res.append(expression[i])
            i += 1
        
        #The element is an operator 
        elif is_operator(expression[i]):    
            while (len(stack_ope) > 0 and is_operator(stack_ope[-1])): #Check the ope stack
                ope_on_top = stack_ope[-1]
                if (priority(expression[i]) <= priority(ope_on_top) and is_associative(expression[i])):
                    stack_res.append(ope_on_top)
                    stack_ope.pop()
                else:
                    break
               
            stack_ope.append(expression[i])
            i += 1
        
        #The element is the beginning of an expression 
        elif expression[i] == '(':
            stack_ope.append(expression[i])
            i += 1
        
        #The element show the end of an expression
        elif expression[i] == ')':        
            while(len(stack_ope) != 0 and stack_ope[-1] != '('):                
                stack_res.append(stack_ope[-1])
                stack_ope.pop()                     
                
            if (stack_ope[-1] == '('):
                stack_ope.pop()
    
    #Emptying last elements of the ope stack to the final stack
    while(len(stack_ope) != 0):
        stack_res.append(stack_ope.pop())
    
    return stack_res

#Checking the operator, do the operation between 2 numbers
def apply_operation(operator, operand_a, operand_b):
    if   operator == '+':
        return operand_a + operand_b
    elif operator == '-':
        return operand_a - operand_b
    elif operator == '/':
        #Check for division by 0
        if (operand_b == 0):
            error_case("Division par 0 !!")
        return operand_a / operand_b
    elif operator == '*':
        return operand_a * operand_b
    elif operator == '%':
        return operand_a % operand_b
    else:
        error_case("Probleme dans l'operation entre :" + str(operand_a) + " et :" + str(operand_b))

#Calculate the result of the RPN notation 
def eval_rpn(rpn_expr):
    stack = []
    
    #Explore the RPN expression with a stack
    for token in rpn_expr:
        if isinstance(token, int):
            stack.append(token)
            
        elif is_operator(token):
            #Reverse poppin to get the right order
            operand_b = stack.pop()
            operand_a = stack.pop()
            result = apply_operation(token, operand_a, operand_b)
            stack.append(result)
    
    return stack[0]

#Get the arithmetical expression 
string_expression = arguments[0]
#Dividing the expression by token 
tokens = lexer(string_expression)
#Transform the arithmetic expr in Reverse Polish Notation
rpn_notation = shunting_yard(tokens)
#Apply the resolution of a postfix notation 
result = eval_rpn(rpn_notation)
#Display the result
print(result)