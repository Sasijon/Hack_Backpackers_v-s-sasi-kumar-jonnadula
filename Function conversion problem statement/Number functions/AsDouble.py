def AsDouble(i):
    
    #toDouble is present in Azure data factory 
    return toDouble(i)
    
    
        
if __name__ == "__main__":

    op = AsDouble(56/4.32)
    print (op)
        