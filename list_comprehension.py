
list =  [1,2,3,4,5]

newList = [n+1 for n in list]

print(newList)

slist = ['a', 'b']

newSlist = [s+'r' for s in slist]
print(newSlist)

string = 'Arv'

strlist = [s for s in string]

print(strlist)

doubled = [n*2 for n in range(1,5)]
print(doubled)


# conditional

names = ['arv','aravind','wrongone','arvind','tanjiro','naruto']

newNames = [n for n in names if n.startswith('a')]
newNames2 = [n for n in names if len(n) > 3]
ch = [n.upper() for n in names if len(n) > 4]
print(newNames, newNames2, ch)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(s) for s in list_of_strings]
result = [n for n in numbers if n%2==0]
print(result)



with open('./file1.txt') as f1:
    d1_raw = f1.readlines()
    d1 = [int(s.strip()) for s in d1_raw]
    with open('file2.txt') as f2:
        d2_raw = f2.readlines()
        d2 = [int(s.strip()) for s in d2_raw]
        common = [n for n in d1 if n in d2]
        print('common:',common)
