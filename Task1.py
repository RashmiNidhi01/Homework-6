import re
import nltk
from nltk import tokenize

nltk.download("punkt")

with open("input.txt", encoding='utf8') as f:
    input_txt = f.readlines()
input_txt = [x.strip() for x in input_txt]

# Dropping all the emtpy elements in the list
input_lines = [i for i in input_txt if len(i)!= 0]

# Total character count
character_count = 0
word_count = 0
word_length = 0
sentence_length = 0
sentence_count = 0

words_ending_ly = []
top_10_words = []
for line in input_lines:
    character_count += len(line)
    # Removing addition words
    words = [i for i in line.split(" ") if len(i)!= 0]
    # Cleaning up words by removing period, braces, full colon etc
    words = [re.sub(r'[\,\.\"\(\)\!\;\:\?\—]',"", i) for i in words if len(i)!= 0]
    word_count += len(words)
    
    for word in words:
        word_length += len(word)
        word = word.lower()
        if word.endswith("ly"):
            words_ending_ly.append(word)
    
    # Breaking up senstences require complicated rules to be applied to using a package to do the same
    sentences = tokenize.sent_tokenize(line)
    
    sentence_count += len(sentences)
    
    for sentence in sentences:
        sentence_length += len(sentence)
        
    top_10_words.extend(words)
    top_10_words.sort(key=len, reverse=True)
    top_10_words = top_10_words[:10]

# Distribtuion of words ending with ly
words_ending_ly_dist_dict = {}
for word in set(words_ending_ly):
    no_words = words_ending_ly.count(word)
    words_ending_ly_dist_dict[word] = no_words
    
# Saving the output
with open("summary.txt", "w") as f:
    #Total word count:
    f.write("Total word count: "+str(word_count)+"\n")
    #Total character count:
    f.write("Total character count: "+str(character_count)+"\n")
    #The average word length:
    f.write("The average word length: "+str(round(1.0*word_length/word_count, 2))+"\n")    
    #The average sentence length:
    f.write("The average sentence length: "+str(round(1.0*sentence_length/sentence_count, 2))+"\n")
    f.write("\n")
    
    #A word distribution of all words ending in “ly”
    f.write('A word distribution of all words ending in “ly”\n')
    for word in words_ending_ly_dist_dict.keys():
        word_freq = words_ending_ly_dist_dict[word]
        f.write(word+": "+str(word_freq)+"\n")
    f.write("\n")

    #A list of top 10 longest words in descending order:
    f.write("A list of top 10 longest words in descending order:\n")
    f.write(", ".join(top_10_words))    
