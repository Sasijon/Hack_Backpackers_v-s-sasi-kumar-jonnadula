import xml.dom.minidom as xdm
from pprint import pprint

data = xdm.parse("test.xml")
mappings = data.getElementsByTagName("MAPPING")

for i in mappings:
    connectors = i.getElementsByTagName("CONNECTOR")
    l = []
    d = {}
    source_list = []
    sq_list = []
    exp_list = []
    next_sq_list = []
    update_strategy_list = []
    target_list = []

    lis = []
    for i in connectors:
        d["FROMINSTANCE"] = i.getAttribute("FROMINSTANCE")
        d["FROMFIELD"] = i.getAttribute("FROMFIELD")
        d["TOINSTANCE"] = i.getAttribute("TOINSTANCE")
        d["TOFIELD"] = i.getAttribute("TOFIELD")

        if i.getAttribute("FROMINSTANCETYPE") == u'Source Definition' and i.getAttribute(
                "TOINSTANCETYPE") == u'Source Qualifier':
            source_list.append(i)
        if i.getAttribute("FROMINSTANCETYPE") == u'Source Qualifier':
            sq_list.append(i)
        if i.getAttribute("FROMINSTANCETYPE") == u'Expression':
            exp_list.append(i)
        if i.getAttribute("FROMINSTANCETYPE") == u'Update Strategy':
            update_strategy_list.append(i)
        if i.getAttribute("TOINSTANCETYPE") == u'Target Definition':
            target_list.append(i)

        # s = set(lis.append(i.getAttribute("FROMINSTANCETYPE")))
        lis.append(i.getAttribute("FROMINSTANCETYPE"))
        lis.append(i.getAttribute("TOINSTANCETYPE"))
        l.append(d)

    d_source = {}
    d_sq = {}
    d_exp = {}
    d_us = {}
    for x in set(source_list):
        d_source[x.getAttribute("FROMINSTANCE").lower()] = [k.getAttribute("FROMFIELD") for k in source_list if
                                                    k.getAttribute("FROMINSTANCE") == x.getAttribute("FROMINSTANCE")]
    for x in set(sq_list):
        d_sq[x.getAttribute("FROMINSTANCE").lower()] = [k.getAttribute("FROMFIELD") for k in sq_list if
                                                k.getAttribute("FROMINSTANCE") == x.getAttribute("FROMINSTANCE")]

    for x in set(exp_list):
        d_exp[x.getAttribute("FROMINSTANCE").lower()] = [k.getAttribute("FROMFIELD") for k in exp_list if
                                                 k.getAttribute("FROMINSTANCE") == x.getAttribute("FROMINSTANCE")]
    for x in set(update_strategy_list):
        d_us[x.getAttribute("FROMINSTANCE").lower()] = [k.getAttribute("FROMFIELD") for k in update_strategy_list if
                                                k.getAttribute("FROMINSTANCE") == x.getAttribute("FROMINSTANCE")]

    for x in set(target_list):
        d_us[x.getAttribute("TOINSTANCE").lower()] = [k.getAttribute("TOFIELD") for k in target_list if
                                                k.getAttribute("TOINSTANCE") == x.getAttribute("TOINSTANCE")]

    # pprint([x.getAttribute("TOINSTANCE") for x in sq_list])
    for k, v in d_source.items():
        fs = 'source(' + k + '.' + str(v) + ')'
        if 'sq_'+k in d_sq.keys():
            fs = fs + '-> source Qualifier(' + 'sq_'+k + '.' + str(d_sq.get('sq_'+k)) + ')'
        if 'exp_'+k in d_exp.keys():
            fs = fs + '-> expression(' + 'exp_'+k + '.' + str(d_exp.get('exp_'+k)) + ')'
        if 'upd_'+k in d_us.keys():
            fs = fs + '-> update s(' + 'upd_'+k + '.' + str(d_us.get('upd_'+k)) + ')'
        if 'upd_'+k in d_us.keys():
            fs = fs + '-> target s(' + 'upd_'+k + '.' + str(d_us.get('upd_'+k)) + ')'
        print(fs)
        print('%%%%%%%%%%%%%%%%%')
        print(d_source.keys(), '|', d_sq.keys(), '|', d_exp.keys(), '|', d_us.keys())
        print('*******')
    print('=============================================')
