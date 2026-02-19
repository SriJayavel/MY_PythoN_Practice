
text = "Testing...Testing...Testing...\nadding text without overwriting the file done\n "


with open('test.txt','a') as file:
    file.write(text)