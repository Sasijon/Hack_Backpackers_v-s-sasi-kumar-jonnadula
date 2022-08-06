from datetime import date
def TimetFromTimestamp(today)
    dt = today
    #dt.timestamp converts to epoch time
    #toTime stamp converts in adf format
    return toTimestamp(dt.timestamp()1000l)
    
    
    
    
'''
TimetFromTimestamp
Returns a UNIX time_t value from the given timestamp.
Input timestamp
Output timet (int32)
Examples. If mylink.mytimestamp contains the value 2009–02–13 233130, then the two following functions are equivalent, and return the value 1234567890 in datastage
'''

today = date.today()
print(TimetFromTimestamp(today))
        