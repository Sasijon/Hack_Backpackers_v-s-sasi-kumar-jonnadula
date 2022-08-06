def Adf_conversion_for_Field_in_datastage(s,delimiter):
    
    r = s.replace('|',',')
    return r
    
    
        
if __name__ == "__main__":
    
    '''
    FIELD (string, delimiter, occurrence [ ,num.substr] ) in data stage
    
    empno,name,dept_details,salary
    123,Naveen,10|Accounts|Chicago|Illinois,10000
    234,Bob,20|Technology|Dallas|Texas,20000
    456,Max,10|Accounts|Chicago|Illinois,30000
    567,Antony,20|Technology|Dallas|Texas,10000
    
    Field(before_xfrm.dept,'|',1) - depid
    Field(before_xfrm.dept,'|',2) - deptname
    Field(before_xfrm.dept,'|',3) - deptcity
    Field(before_xfrm.dept,'|',4) - deptstate
    
    '''
    s = '123,Naveen,10|Accounts|Chicago|Illinois,10000'
    delimiter = '|'
       
    op = Adf_conversion_for_Field_in_datastage(s,delimiter)
    print (op)
        