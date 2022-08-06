def get_originating_tables(sql_script):
    sql_script.strip() # Removes spaces
    d = {} # dictionary for  storing column values
    
    #fetching indexes from select and from
    idx_columns_select = sql_script.find('SELECT') + 6
    idx_columns_from = sql_script.find('FROM')
    
    
    
    #creating a list
    columns = sql_script[idx_columns_select:idx_columns_from:].strip()
    lis = columns.split(',')
    
    
    
    for i in range(len(lis)):
        temp = lis[i].split('.')
        d[temp[1]] = temp[0].strip()
    
    idx_columns_ending = sql_script.find(';')
    
    tables = sql_script[idx_columns_from:idx_columns_ending:]
    tables.strip()
    lis_tables = tables.split(',')
    dic_tables = {}
    for i in range(len(lis_tables)):
        idx_opening_bracket = lis_tables[i].find('(')
        idx_closing_bracket = lis_tables[i].find(')')
        temp = lis_tables[i][idx_opening_bracket:idx_closing_bracket:].split(' ')[-1]
        
        dic_tables[lis_tables[i][-1]] =  temp.strip()
    
    for key,value in d.items():
        d[key] = dic_tables[value]
    op_list = ['column => table']
    for key,value in d.items():
        op_list.append(key + ' => ' + value)
    
    
    return op_list
    
sql_script = "SELECT a.uid, b.uname FROM (select * from user) a,(select * from user_details) b;"


for x in get_originating_tables(sql_script):
    print(x)