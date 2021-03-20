import re

b = ' '.join(a+b for a,b in zip(datatoarray2[::2], datatoarray2[1::2])) #splits string to every 2 characters
# print("Data before stuff2: ",b)

replacements = {'7e': '7d 5e', '7d': '7d 5d'}
stuffing1 = re.sub('({})'.format('|'.join(map(re.escape, replacements.keys()))), lambda m: replacements[m.group()], b) # replaces for HDLC frame sequence
# print("Data after stuff2: ", stuffing1)

spaceaway3 = stuffing1.replace(" ", "") # joins string back together