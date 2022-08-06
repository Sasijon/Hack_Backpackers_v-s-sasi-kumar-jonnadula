def MantissaFromDecimal(i):
    
    #tostring is present in azure data factory
    return toString(i,indexOf(i,'.'))
    
    
    
        
if __name__ == "__main__":

    op = MantissaFromDecimal('243.7675')
    print (op)
        