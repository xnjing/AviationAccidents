from collections import defaultdict
import operator
#import csv
#f = open("AviationData.txt")
#aviation_data = f.readline()
#aviation_list = []
#for line in aviation_data:
#    aviation_list.append(line.split(" | "))


aviation_data = [x for x in open("AviationData.txt")]
aviation_list = [x.split(" | ") for x in aviation_data]
lax_code = []
for row in aviation_list:
    if "LAX94LA336" in row:
        lax_code.append(row)
print(lax_code)

header = aviation_list[0]
aviation_dict_list = [dict(zip(header, row)) for row in aviation_list[1:]]
lax_dict = [row for row in aviation_dict_list if "LAX94LA336" in row.values()]
print(lax_dict)

state_accidents = defaultdict(int)
for row in aviation_dict_list:
    if row['Country'] == 'United States' and ", " in row['Location']:
        state = row["Location"].split(', ')[1]
        state_accidents[state]  += 1
state_accidents = dict(state_accidents)
most_accident_state = max(state_accidents.items(),key=operator.itemgetter(1))[0]
print(most_accident_state)

monthly_injuries = defaultdict(lambda: [0,0])
#monthly_injuries = defaultdict(list)
for row in aviation_dict_list:
    month = row['Event Date'].split("/")[0]
    for idex, case in enumerate(['Total Fatal Injuries', 'Total Serious Injuries']):
        if row[case] != '':
            monthly_injuries[month][idex] += int(row[case])
        else:
            monthly_injuries[month][idex] += 0

print(monthly_injuries)



