import json
output = open("params.new.pd", "w")
read_file = open("module.json", "r")
data = json.load(read_file)

lines = []
lines.append("#N canvas 0 25 1034 552 12;\n")

lines.append("#X obj 280 268 outlet;\n");


start = 22;
for param in data['parameters']:
	lines.append("#X obj 109 " + str(start) + " r " + param[1] + "-\$1;\n")
	start = start + 20
	lines.append("#X obj 109 " + str(start) + " float;\n")
	start = start + 20
	lines.append("#X msg 109 " + str(start) + " " + param[1] + "-pd \$1;\n")
	start = start + 20

lines.append("#X obj 240 240 inlet;\n");

for i in range(0, len(data['parameters'])):
	start = str(i*3+1)
	fl = str(i*3+2)
	end =  str(i*3+3)
	inlet = str(len(data['parameters'])*3+1)
	lines.append("#X connect " + start + " 0 " + fl +" 0;\n")
	lines.append("#X connect " + fl + " 0 " + end +" 0;\n")
	lines.append("#X connect " + end + " 0 0 0;\n")
	lines.append("#X connect " + inlet + " 0 " + fl +" 0;\n")



output.writelines(lines)
