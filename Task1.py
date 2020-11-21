import sys
import string
import os

read_file='content.txt'
read_mode='r'
write_file='summary.txt'
write_mode='w'

char_count = {}
line_count={}
sent_count={}
word_count={}
ly_endict={}
ten_longword_dict={}
lon_wordict={}

try:
    file = open("content.txt", "r") # open file read mode
    file= open("summary.txt", "w") # open file write mode
    validchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # only these counted
    if len(line.split())==0:
        continue
sentence = sentence.split(" ")
sent_count+==len(sentence)
line=l.lower()
line=l.translate(line.maketrans("", "", string.punctuation))
line=l.replace('-','')
linecount[c] += 1

words = words.split(" ")
word_count+=len(words)
char_count+=sum(len(char) for char in words)
max_len=len(max(words, key=len))

for long_word in line.split():
    if len(long_word) == max_len:
                    if long_word not in lon_wordict:
                        lon_wordict[long_word] = len(long_word)
    if long_word.endswith('ly'):
                    if long_word in ly_endict:
                        ly_endict[long_word] += 1
                    else:
                        ly_endict[long_word] = 1



        file.write(f'Total word count: {word_count}\n')
        file.write(f'Total character count: {char_count}\n')
        file.write(f'The average word length: {(char_count/word_count):.2f}\n')
        file.write(f'The average sentence length: {(word_count/sent_count):.2f}\n')
        file.write('\n')

        
        file.write('A word distribution of all words ending in “ly”\n')
        for ly_end_word,count in sorted(ly_endict.items()):   
            file.write(f'{ly_end_word}: {count}\n')
        file.write('\n')
        
        
        file.write('A list of top 10 longest words in descending order:\n') 
        ten_longword_dict = {long_word: count for long_word,count in sorted(ly_endict.items(),key = lambda x: x[1],reverse = True)}
        for long_words in sorted(list(ten_longword_dict)[0:10],reverse = True): 
            file.write(f'{long_words}, ')
