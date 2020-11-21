import string

# Reading the file
with open("book.txt") as f:
    book = f.read()
book = book.lower()
    
lowercase_alphabets = string.ascii_lowercase   
alphabet_count_dict = {}

for alphabet in lowercase_alphabets:
    alphabet_freq = list(book).count(alphabet)
    
    if alphabet_freq != 0:
        alphabet_count_dict[alphabet] = alphabet_freq
        
# Saving the output
# Saving the output
with open("summary2.txt", "w") as f:
    
    for key in sorted(alphabet_count_dict.keys()):
        alphabet_freq = alphabet_count_dict[key]
        f.write(key.upper()+" "+str(alphabet_freq)+"\n")
    
    f.write("\n")
    
    if len(alphabet_count_dict.keys()) != 26:
        f.write("It doesn't have all letters.")
    else:
        f.write("It has all letters.")