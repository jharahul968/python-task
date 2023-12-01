import json

file=open('/resources/weather.json')

data=json.load(file)



# filtering data


max_temp_list=[]

for i in data:
    max_temp_list.append(i["MaxTemp"])
    
file.close()

print(max_temp_list)