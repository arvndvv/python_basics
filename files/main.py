with open('./files/text.txt','w') as file:
    file.write('Hello\n')
    file.write('World\n')

with open('./files/text.txt','r') as file:
    contents = file.read()
    print(contents)