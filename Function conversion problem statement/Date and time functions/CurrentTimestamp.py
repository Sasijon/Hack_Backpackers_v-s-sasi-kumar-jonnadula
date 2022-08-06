def Adf_conversion_for_CurrentTimeStamp_in_datastage(s):
    lis = s.split('T')
    return lis[0] + ' ' + lis[1].split('.')[0]
    
    

if __name__ == "__main__":
    #utc_now() in adf
    utc_now =  '2021-09-01T19:55:07.0000000Z'
    #CurrentTimestamp() in datastage '2021-09-01 19:55:07'
  
    op = Adf_conversion_for_CurrentTimeStamp_in_datastage(utc_now)
    print (op)
        