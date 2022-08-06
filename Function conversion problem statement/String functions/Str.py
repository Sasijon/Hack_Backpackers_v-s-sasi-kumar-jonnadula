def Adf_conversion_for_Str_in_datastage(s,N):
    lis = [s] * N
    return join(lis,'')
    
    
        
if __name__ == "__main__":
    s = 'A'
    N = 10
    op = Adf_conversion_for_Str_in_datastage(s,N)
    print (op)
        