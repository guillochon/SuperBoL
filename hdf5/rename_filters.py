from tables import *

h5file = open_file('sn_data.h5', 'a')

table = h5file.root.filters

table.cols.name[0] = 'B'
table.cols.name[1] = 'V'
table.cols.name[2] = 'I'
table.cols.name[3] = 'clear'
table.cols.name[4] = 'U'
table.cols.name[5] = 'B'
table.cols.name[6] = 'V'
table.cols.name[7] = 'R'
table.cols.name[8] = 'I'
table.cols.name[9] = 'U'
table.cols.name[10] = 'B'
table.cols.name[11] = 'V'
table.cols.name[12] = 'R'
table.cols.name[13] = 'I'
table.cols.name[14] = 'R'
table.cols.name[15] = 'B'
table.cols.name[16] = 'V'
table.cols.name[17] = 'R'
table.cols.name[18] = 'I'
table.cols.name[19] = 'B'
table.cols.name[20] = 'V'
table.cols.name[21] = 'R'
table.cols.name[22] = 'I'
table.cols.name[23] = 'U'
table.cols.name[24] = 'B'
table.cols.name[25] = 'V'
table.cols.name[26] = 'R'
table.cols.name[27] = 'I'
table.cols.name[28] = 'J'
table.cols.name[29] = 'H'
table.cols.name[30] = 'K'
table.cols.name[31] = 'J'
table.cols.name[32] = 'H'
table.cols.name[33] = 'K'
table.cols.name[34] = 'u'
table.cols.name[35] = 'g'
table.cols.name[36] = 'r'
table.cols.name[37] = 'i'
table.cols.name[38] = 'B'
table.cols.name[39] = 'V'
table.cols.name[40] = 'Y'
table.cols.name[41] = 'J'
table.cols.name[42] = 'H'
table.cols.name[43] = 'u'
table.cols.name[44] = 'g'
table.cols.name[45] = 'r'
table.cols.name[46] = 'i'
table.cols.name[47] = 'B'
table.cols.name[48] = 'V'
table.cols.name[49] = 'Y'
table.cols.name[50] = 'J'
table.cols.name[51] = 'H'
table.cols.name[98] = 'z'
table.flush()

h5file.close()