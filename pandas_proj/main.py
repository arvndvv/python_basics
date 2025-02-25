import pandas

data = pandas.read_csv('./weather_data.csv')
temp_data = data["temp"]
print(temp_data)
data_temp_list = temp_data.to_list()
# total_temp = 0
# calculate total using for loop
# for temp in data_temp_list:
#     total_temp += temp
# calculate using sum function
# total_temp = sum(data_temp_list)
# average_temp = total_temp / len(data_temp_list)
# print(average_temp)
# using pandas inbuilt mean() function
print('mean:',temp_data.mean())
print('max:',temp_data.max())

# get columns 2 ways
print(data['temp'])
print(data.temp)

# get a row based on condition

row_data = data[data.day == 'Monday']

print(row_data)

# get row having max temp

max_temp_row = data[data.temp == data.temp.max()]

print(max_temp_row)

# get mondays row, convert temp to farenheit
def c_to_f(c):
    return ((c * (9/5)) + 32)

monday_row = data[data.day=="Monday"]
monday_temp = c_to_f(monday_row.temp)
print(monday_temp)


# create a dataframe from scratch

data_dict = {
    "names":["arv","ind"],
    "emails":["arv@gmail.com",'ind@gmail.com']
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame)

# save as csv

data_frame.to_csv('./arv.csv')