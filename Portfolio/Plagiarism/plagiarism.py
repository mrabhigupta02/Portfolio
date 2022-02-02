# Plagiarism detection by manuallay
# There in this project i made a plagiarism detector by two methods
# 1--->>> Manually by comparision
# 2--->>> by use of SequenceMatcher


# reading files
file1 = open("file_1.txt",'r')
file2 = open('file_2.txt','r')

file_1 = file1.readlines()
file_2 = file2.readlines()

#joining
sen_file_1 = ''.join(file_1)
sen_file_2 = ''.join(file_2)

# spliting by lines
file1ByLines = sen_file_1.split('.')
file2ByLines = sen_file_2.split('.')

plag = []


for i in file1ByLines:
    for j in file2ByLines:
        if i==j:
            plag.append(i)
percentage = len(plag)/len(file1ByLines)*100

print(plag)


# Plagiarism by SequenceMatcher
from difflib import SequenceMatcher

print(" ")
print(" ")
Similarity = SequenceMatcher(None, file_1, file_2).ratio()
print(f"Percentage by using of sequenceMatcher = {Similarity*100}%")
print(f"Plagiarism percentage is manual matching = {percentage} %")