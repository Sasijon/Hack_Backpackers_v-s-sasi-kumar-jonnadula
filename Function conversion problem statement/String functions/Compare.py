def Adf_conversion_for_Compare_in_datastage(s1,s2,justification):
    num1 = ''
    num2 = ''
    char1 = ''
    char2 = ''
    
    for x in s1:
        if x.isnumeric() == True:
            num1 = num1 + x
        elif x.isalpha() == True:
            char1 = char1 + x
    for x in s2:
        if x.isnumeric() == True:
            num1 = num1 + x
        elif x.isalpha() == True:
            char1 = char1 + x
            
            
    
    if justification == 'L':
        if char1 > char2 :
            return 1
        elif char1 < char2 :
            return -1
        else:
            return 0
    elif justification == 'R':
        if num1 > num2 :
            return 1
        elif num1 < num2 :
            return -1
        else:
            return 0
        
if __name__ == "__main__":
    
    '''
    Compare("AB99", "AB100", "R")
    Compare (string1, string2  [ , justification ] ) in data stage
    
    -1 string1 is less than string2.

    0 string1 equals string2 or the justification expression is not valid.

    1 string1 is greater than string2.
    
    '''
    s1 = 'AB99'
    s2 = 'AB100'
    justification = 'R'
   
    op = Adf_conversion_for_Compare_in_datastage(s1,s2,justification)
    print (op)
        