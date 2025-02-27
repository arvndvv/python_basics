import pandas
list_2 = [1,2,3,5]

new_dict = {'num'+str(n):n for n in list_2}
print(new_dict)

another_dict = {key:value+1 for (key, value) in new_dict.items()}

print(another_dict)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
s_list = sentence.split(' ')
result = {k:len(k) for k in s_list}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {k:(v * 9/5)+32 for (k,v) in weather_c.items()}

print(weather_f)

test_dict = {
    "students": ['a','b'],
    "marks":[1,2]
}

pandas_dict = pandas.DataFrame(test_dict)
# print(pandas_dict)

for (index, row) in pandas_dict.iterrows():
    print(row.marks)

ex = {index:row for (index,row) in pandas_dict.iterrows()}
print(ex)



name = input('what is your name?')
char_list = list(name)
phonetics = pandas.read_csv('nato_phonetic_alphabet.csv')
itter = phonetics.iterrows()

phonetics_dict = {v.letter:v.code for (index,v) in itter}
# print(phonetics)
# print('test',phonetics_dict,phonetics.to_dict())

updated_name_list = [phonetics_dict[char.upper()] for char in char_list]
joined = ' '.join(updated_name_list)
print(joined)