def Adf_conversion_for_AlNum_in_datastage(s):
    if s.isalnum():
        return True
    else:
        return False
    
    
    
    

if __name__ == "__main__":
    
    '''
    AlNum in datastage AlNum('123abc') output is True/False
    Alnum(“12345”) ---> output-True
    Alnum(“abcd”) ---> output-True
    Alnum(“ab125”) ---> output-True
    Alnum(“@a12345”) ---> output-False
    Alnum(“@a1 2345”) ---> output-False
    
    '''
    s = '@a1 2345'
    op = Adf_conversion_for_AlNum_in_datastage(s)
    print (op)
        