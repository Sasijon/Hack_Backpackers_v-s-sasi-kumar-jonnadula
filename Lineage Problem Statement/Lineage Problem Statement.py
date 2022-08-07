

def get_originating_tables(sql_script):
    regex = "(.)"
    sql_script.strip() # Removes spaces
    d = {} # dictionary for  storing column values
    
    #fetching indexes from select and from
    idx_columns_select = sql_script.find('SELECT') + 6
    idx_columns_from = sql_script.find('FROM')
    
    
    
    #creating a list
    columns = sql_script[idx_columns_select:idx_columns_from:].strip()
    lis = columns.split(',')
    lis = [x.strip('\n') for x in lis]

    
    
    
    
    for i in range(len(lis)):
        temp = lis[i].split('.')
        d[temp[1]] = temp[0].strip()

    
    closing_bracket_index = []
    tables_alias = list(set([x for x in d.values()]))
    open_bracket_list_idx = []
    substrings = [] 
    for i in range(len(sql_script)):
        if sql_script[i] == '(':
            open_bracket_list_idx.append(i)
        if sql_script[i] == ')':
            temp = sql_script[open_bracket_list_idx.pop(-1)+1:i:]
            substrings.append(temp)


    substrings = [x.replace('\n', ' ').upper() for x in substrings if 'select' in x.lower()]
    subquery_table = {}
    for x in substrings:
        idx_1 = sql_script.find(x) + len(x)
        temp = x.split(' ')
        idx_2 = temp.index('FROM')
        k = True
        while(k == True):
            if sql_script[idx_1 + 1] in tables_alias:
                subquery_table[sql_script[idx_1 + 1]] =   temp[idx_2 + 1]
                k = False
            idx_1 = idx_1 + 1

        
   
    
  

    
    
    
    for key,value in d.items():
        d[key] = subquery_table[value]
    op_list = ['column => table']
    for key,value in d.items():
        op_list.append(key + ' => ' + value)
    return op_list
    


    
sql_script = """" LOCKING ROW FOR ACCESS
SELECT

T.SWB_CNTRY_ID,

T.CNTRY_TYPE_CD,

T.DW_EFF_OT,

S.DW_AS_OF_DT

FROM

(SELECT

SWB_CNTRY_ID,

CNTRY_TYPE_CD,

RCV_IN,

DW_EFF_DT,

MAX(DW_EFF_DT) MAX_EFF_DT

FROM IDW_DATA.CNTRY_MULTI_DEF_CD_T

WHERE

CURR_IN=1 GROUP BY 1,2,3,4) T,

(SELECT

SWB_CNTRY_ID,

CNTRY_SCHEME_CD,

DW_AS_OF_DT,

DW_ACTN_IND

FROM IDW_STAGE.CNTRY_MULTI_DEF_CD_S) S

WHERE

S.SWB_CNTRY_ID = T.SWB_CNTRY_ID AND S.CNTRY_SCHEME_CD = T.CNTRY_TYPE_CD
AND (S.DW_ACTN_IND='U' OR (S.DW_ACTN_IND='I" AND T.RCV_IN = 0))
AND S.DW_AS OF DT > T.MAX_EFF_DT"""

for x in get_originating_tables(sql_script):
    print(x)
