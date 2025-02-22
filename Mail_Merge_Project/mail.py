#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Mail_Merge_Project/Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    for name in names_list:
        name = name.strip()
        with open('./Mail_Merge_Project/Input/Letters/starting_letter.txt') as letter:
            letter_content = letter.read()
            updated_letter = letter_content.replace('[name]',name)
            print(updated_letter)
            with open(f'./Mail_Merge_Project/Output/ReadyToSend/letter_for_{name}.txt',mode='w') as completed_letter:
                completed_letter.write(updated_letter)
