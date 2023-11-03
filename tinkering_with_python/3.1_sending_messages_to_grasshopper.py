# run "pip install pygame" in terminal
# make sure you're in the same folder as this file!

def write_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

write_to_file('data.txt', '! SelAll Delete Enter !')
        
