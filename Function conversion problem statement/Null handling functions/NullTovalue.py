def NullToValue(m,i):
    #isNull is  present in azure data factory
    if isNull(m) == True:
        return i
    else:
        return m
    
    
    
        
if __name__ == "__main__":
    
    '''
    NullToValue(m,42) in data stage
    '''
    m = None
    default_value = 10
    op = NullToValue(m,default_value)
    print (op)
        