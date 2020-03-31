TEXT_FILE = open('file.txt',mode='r')
first_line = TEXT_FILE.readline()
print(first_line)

all_text = TEXT_FILE.read()
print(all_text)
TEXT_FILE.close()

with open('file.txt','r') as text_file_2:
    print(text_file_2.read())