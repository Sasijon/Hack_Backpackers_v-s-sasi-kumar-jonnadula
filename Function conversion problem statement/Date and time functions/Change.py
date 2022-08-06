def Adf_conversion_for_Change_in_datastage(s,old_value,new_value,occurence):
    return s.replace(old_value,new_value,occurence)
    
    
    
    
    

if __name__ == "__main__":
    
    '''
    CHANGE (expression, substring, replacement [ ,occurrence [ ,begin] ] 
) in data stage

    replace('the old string', 'old', 'new') is present in adf
    op:- 'the new string'
    
    s = "AAABBBCCCDDDBBB"
    CHANGE (s,"BBB","ZZZ") -> AAAZZZCCCDDDZZZ
    CHANGE (s,"","ZZZ") -> AAABBBCCCDDDBBB
    CHANGE (s,"BBB","") -> AAACCCDDD
    
    '''
    s = 'AAABBBCCCDDDBBB'
    old_value = 'BBB'
    new_value = 'ZZZ'
    occurence = 1
    op = Adf_conversion_for_Change_in_datastage(s,old_value,new_value,occurence)
    print (op)
        