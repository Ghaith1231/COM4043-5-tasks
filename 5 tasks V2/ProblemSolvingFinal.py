def calFunc(values, weights):
    total_weight = sum(weight)
    # total = 10  # left this here when editing, to be checked before committing
    for i in range(len(value)):
        total += values[i] * weight[i]
    out1 = total / total_weights
    return out1

# Main program
Variable1 = ['60', '70', '60', {40}]
weights = [15, 20, 30, '15']

print("The output is:", CalFunc(Variable1, weights))

calFunc()

# debug/fixes and suggestions for improvements

def calFunc(values, weights):
    total_weight = sum(weights)  # correcting (was "weight") the spelling and making it plural 
    total = 0  # initializing the total variable to 0 before the loop
    
    for i in range(len(values)):  # correcting to "values" and defining "i"
        total += int(values[i]) * int(weights[i])  # corrected to "weights" also corrected to integers to have value
    
    out1 = total / total_weight  # corrected to "total_weight"
    return out1

# main code
Values = ['60', '70', '60', '40']  # removed the string for all the numbers to be included in the equatin and to have3 no error code / inaccurate results and using "values" as the list of the values 
weights = ['15', '20', '30', '15']  # same as above

print("The output is:", calFunc(Variable1, weights))  # corrected the function name to call

# i also improved the structure of the code from the original 

#Improvements that should be considered for the future:
#1. Error checking: The code does not check if the input are correct and would suggest to double look for any  errors or typos in the future and check they have the same lenght
#  Example  return "Error: 'values' and 'weights' must have the same length."
#2. add error notes so you can warn the user of of invalid input.
# Example  return "Error: the weight cannot be 0 or below."
# 3. Add a check to make sure all inputs are numbers.
# Example 0 cannot be devided by 0
#4. you can improve your code by using 'if' or 'try' to imrove your code
# Example if len(values) != len(weights):




# explanation of the code 

# this function uses 2 lists called 'values' and 'wights' 
# it calculates both of the values from 'wights' and 'values' and ads them together.
# it then divides the total by the sum of the 'wights' list to get the average.
# thid is useful when some values are rated higher/more important than others
# like final grade (to calculate student results) or financial data ( used for businesses to calculate there finance)

def calFunc(values, weights):
    total_weight = sum(weights) # sum of the weights
    total = 0  # start with the base number of 0 
    
    for i in range(len(values)):  # loop running through each value
        total += int(values[i]) * int(weights[i])  # multiple value and weights then add together to get the total   
        
        out1 = total / total_weight # caluclating the average 
    return out1 #return the resluts

# main code
Values = ['60', '70', '60', '40']  # lists of values
weights = ['15', '20', '30', '15']  # list of weights

print("The output is:", calFunc(Variable1, weights))  # corrected spelling to 'values'

#This weighted average function can be used in education to calculate final grades
# where exams are more significant than others like mini group projects
# Similarly, it can be used in finance to caluculate business assits 
