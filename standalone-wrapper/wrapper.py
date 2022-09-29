import json
output = open("params.new.pd", "w")
read_file = open("module.json", "r")
data = json.load(read_file)

lines = []
lines.append("#N canvas 0 25 1034 552 12;\n")



start = 22;
x = 109
increment = 25;
increment_x = 150

for param in data['parameters']:
	y = start
	minval = "0";
	maxval = "1";
	if param[0] != "bool":
		minval = str(param[3]);
		maxval = str(param[4]);
	integertype = param[0] == "bool" or param[0] == "int";

	lines.append("#X obj " + str(x) + " " + str(y) + " hsl 128 15 " + minval + " " + maxval + " 0 0 empty empty empty -2 -8 0 10 -262144-1 -1 10500 1;\n")
	y = y + increment

	if integertype:
		lines.append("#X obj " + str(x) + " " + str(y) + " int;\n")
	else:
		lines.append("#X obj " + str(x) + " " + str(y) + " float;\n")
	y = y + increment
	lines.append("#X floatatom " + str(x) + " " + str(y) + " 10 0 0 0 - - -;\n")
	y = y + increment
	lines.append("#X obj " + str(x) + " " + str(y) + " s " + param[1] + "-pd;\n")
	
	x = x + increment_x
	if( x > 800):
		x = 109
		start += 150



for i in range(0, len(data['parameters'])):
	start = str(i*4)
	fl1 = str(i*4+1)
	fl2 = str(i*4+2)
	end =  str(i*4+3)
	lines.append("#X connect " + start + " 0 " + fl1 +" 0;\n")
	lines.append("#X connect " + fl1 + " 0 " + fl2 +" 0;\n")
	lines.append("#X connect " + fl2 + " 0 " + end +" 0;\n")
	lines.append("#X connect " + end + " 0 0 0;\n")


output.writelines(lines)
