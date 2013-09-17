import re

rex = re.compile(r'<APP_LoTW_MODEGROUP:.+>(.+)\n.+\n<BAND:.+>(.+)\n.+\n<COUNTRY:.+>(.+)', re.MULTILINE)
map = {}
with open('DXCC_QSLs_20130917_055734.adi') as file:
	text = file.read()
	for match in rex.finditer(text):
		group = match.groups()
		if group[2] in map:
			data = map[group[2]]
			data[0] = 1 if group[0] == 'CW' and data[0] == 0 else data[0]
			data[1] = 1 if group[0] == 'PHONE' and data[1] == 0 else data[1]
			data[2] = 1 if group[0] == 'DATA' and data[2] == 0 else data[2]
			data[3] = 1 if group[1] == '80M' and data[3] == 0 else data[3]
			data[4] = 1 if group[1] == '40M' and data[4] == 0 else data[4]
			data[5] = 1 if group[1] == '20M' and data[5] == 0 else data[5]
			data[6] = 1 if group[1] == '15M' and data[6] == 0 else data[6]
			data[7] = 1 if group[1] == '10M' and data[7] == 0 else data[7]
			data[8] = 1 if group[1] == '6M' and data[8] == 0 else data[8]
			data[9] = 1 if group[1] == '2M' and data[9] == 0 else data[9]
		else:
			cw = 1 if group[0] == 'CW' else 0
			phone = 1 if group[0] == 'PHONE' else 0
			data = 1 if group[0] == 'DATA' else 0
			m80 = 1 if group[1] == '80M' else 0
			m40 = 1 if group[1] == '40M' else 0
			m20 = 1 if group[1] == '20M' else 0
			m15 = 1 if group[1] == '15M' else 0
			m10 = 1 if group[1] == '10M' else 0
			m6  = 1 if group[1] == '6M' else 0
			m2  = 1 if group[1] == '2M' else 0
			map[group[2]] = [cw, phone, data, m80, m40, m20, m15, m10, m6, m2]
			
for key in sorted(map):
	print '%-35s' % key,
	print '%d %d %d  %d %d %d %d %d  %d %d' % (map[key][0],map[key][1],map[key][2],map[key][3],map[key][4],map[key][5],map[key][6],map[key][7],map[key][8],map[key][9])

print '\n%d entries' % len(map)