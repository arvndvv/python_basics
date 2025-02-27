import pandas
data_dict = {
    "names":["arv","ind","arv"],
    "emails":["arv@gmail.com",'ind@gmail.com',"arv2@g.c"]
}

data_frame = pandas.DataFrame(data_dict)
print(data_frame.names[data_frame.names=='arv'].count())
test_count = data_frame.names.value_counts()

# create a csv from squirrels csv with count of unique primary colors
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels =data[data['Primary Fur Color'] == "Gray"]
print(gray_squirrels)
cinnamon_squirrels = data[data['Primary Fur Color'] == "Cinnamon"]
black_squirrels = data[data['Primary Fur Color'] == "Black"]

data_set = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count":[len(gray_squirrels),len(cinnamon_squirrels),len(black_squirrels)]
}
df = pandas.DataFrame(data_set)
df.to_csv('squirrels_count.csv')

# alternative
unique_fur = data['Primary Fur Color'].unique()
print(unique_fur)
unique_count = data['Primary Fur Color'].value_counts()
unique_count.to_csv('test.csv')