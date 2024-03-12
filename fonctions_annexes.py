import sys

########################################
## Functions to print error and exit  ##
########################################
### Print error with detail and exit ###
def error_case(message = ""):
    if (message != ""):
        print("error : " + message)
    else:
        print("error !")
    exit()

########################################
## Functions to print different types ##
########################################
####### Print list line by line ########
def print_list_by_line(list):
    for element in list:
        print(element)

######## Print list in a string ########
def print_list_to_string(list):
    stringRes = ""
    for element in list:
        stringRes += str(element) + ", "
    stringRes = stringRes[0:-2] #Delete the last comma
    print(stringRes)

########################################
## Functions to check the len of args ##
########################################
#Check if a list of args is > len required
def is_args_len_sup(args, lenReqired):
    if (len(args) > lenReqired):
        return True
    else:
        return False

#Check if a list of args is != len required
def is_args_len_diff(args, lenReqired):
    if (len(args) != lenReqired):
        return True
    else:
        return False

#Check if a list of args is < len required
def is_args_len_inf(args, lenReqired):
    if (len(args) < lenReqired):
        return True
    else:
        return False

#########################################
## Functions to check the type of args ##
#########################################
############### For Lists ###############
#Verify all elements are numbers including negatives
def is_args_all_num(arguments):
    for argument in arguments:
        if (not is_num(argument)): #Negative and positive numbers
            return False
    return True

#Verify all elements are numbers excluding negatives
def is_args_all_pos_num(arguments):
    for argument in arguments:
        if (not is_pos_num(argument)): #Only positive numbers
            return False
    return True

#Verify all elements are string
def is_args_all_alpha(arguments):
    for argument in arguments:
        if (not is_alpha(argument)): #Only alpha char
            return False
    return True

########### For single value ###########
#Check if a string value is a positive or negative number
def is_num(argument):
    if (not (argument.startswith("-") and argument[1:].isnumeric()) and not argument.isnumeric()): #Only positive numbers
        return False
    else:
        return True

#Check if a string value is a positive number
def is_pos_num(argument):
    if ((argument.startswith("-") and argument[1:].isnumeric()) or not argument.isnumeric()): #Only positive numbers
        return False
    else:
        return True

#Check if a string value is only only composed by alpha char
def is_alpha(argument):
    if (not argument.isalpha()):
        return False
    else:
        return True
