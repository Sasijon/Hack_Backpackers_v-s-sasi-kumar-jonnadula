def IsNotNull(i):
    #isNull is  present in azure data factory
    if isNull(i) == True:
        return True
    else:
        return False
    
    
    
        
if __name__ == "__main__":
    
    '''
    IsNotNull() in data stage
    Returns true when an expression does not evaluate to the null value.
    Input: any
        Output: true/false (int8)
    '''
    op = IsNotNull('243.7675')
    print (op)
        