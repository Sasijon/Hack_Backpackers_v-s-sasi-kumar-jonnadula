import xml.etree.ElementTree as ET

tree = ET.parse('C:\Users\Latha\OneDrive\Desktop\wf_src_idw_cntry_multi_def_cd.xml')

root = tree.getroot()

source1 = root[0][1][0].attrib
source2 = root[0][1][1].attrib
source3 = root[0][1][2].attrib

target1 = root[0][1][3].attrib
target2 = root[0][1][4].attrib


mapping1 = root[0][0][0].attrib

shortcut_s3 = root[0][0][1].attrib
shortcut_t2 = root[0][0][2].attrib
config_1 = root[0][0][3].attrib

session_1 = root[0][0][4].attrib

mapping_1 = root[0][0][5].attrib
shortcut_s2_dummy = root[0][0][6].attrib

shortcut_s1 = root[0][0][7].attrib

shortcut_t1 = root[0][0][8].attrib

config_2 = root[0][0][9].attrib

session_2 = root[0][0][10].attrib

workflow = root[0][0][11].attrib

transformations1 = root[0][0][0][0].attrib



transformations2 = root[0][0][0][1].attrib


print(root[0].attrib)

