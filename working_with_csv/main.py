# with open('./working_with_csv/weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)

import csv
with open('./working_with_csv/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    print(data)
    temperature_list = []
    for row in data:
        if row[1] != 'temp':
            temperature_list.append(row[1])
    
    print(temperature_list)

